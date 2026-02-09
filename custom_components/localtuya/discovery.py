"""Discovery module for Tuya devices.

Entirely based on tuya-convert.py from tuya-convert:

https://github.com/ct-Open-Source/tuya-convert/blob/master/scripts/tuya-discovery.py
"""
import asyncio
import json
import logging
import struct
from hashlib import md5

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

_LOGGER = logging.getLogger(__name__)

UDP_KEY = md5(b"yGAdlopoPVldABfn").digest()

DEFAULT_TIMEOUT = 6.0


def decrypt_udp(message):
    """Decrypt encrypted UDP broadcasts."""

    def _unpad(data):
        return data[: -ord(data[len(data) - 1 :])]

    cipher = Cipher(algorithms.AES(UDP_KEY), modes.ECB(), default_backend())
    decryptor = cipher.decryptor()
    return _unpad(decryptor.update(message) + decryptor.finalize()).decode()


def decrypt_6699(data):
    """Decrypt 6699-format discovery broadcast."""
    header_fmt = ">IHIII"
    header_len = struct.calcsize(header_fmt)
    _, _, _, _, payload_len = struct.unpack(header_fmt, data[:header_len])
    iv = data[header_len : header_len + 12]
    suffix_offset = header_len + payload_len - 4
    tag = data[suffix_offset - 16 : suffix_offset]
    encrypted = data[header_len + 12 : suffix_offset - 16]
    aad = data[4:header_len]
    cipher = Cipher(algorithms.AES(UDP_KEY), modes.GCM(iv, tag), default_backend())
    decryptor = cipher.decryptor()
    decryptor.authenticate_additional_data(aad)
    return (decryptor.update(encrypted) + decryptor.finalize()).decode()


class TuyaDiscovery(asyncio.DatagramProtocol):
    """Datagram handler listening for Tuya broadcast messages."""

    def __init__(self, callback=None):
        """Initialize a new BaseDiscovery."""
        self.devices = {}
        self._listeners = []
        self._callback = callback

    async def start(self):
        """Start discovery by listening to broadcasts."""
        loop = asyncio.get_running_loop()
        listener = loop.create_datagram_endpoint(
            lambda: self, local_addr=("0.0.0.0", 6666), reuse_port=True
        )
        encrypted_listener = loop.create_datagram_endpoint(
            lambda: self, local_addr=("0.0.0.0", 6667), reuse_port=True
        )
        listener_6699 = loop.create_datagram_endpoint(
            lambda: self, local_addr=("0.0.0.0", 7000), reuse_port=True
        )

        self._listeners = await asyncio.gather(
            listener, encrypted_listener, listener_6699
        )
        _LOGGER.debug("Listening to broadcasts on UDP port 6666, 6667 and 7000")

    def close(self):
        """Stop discovery."""
        self._callback = None
        for transport, _ in self._listeners:
            transport.close()

    def datagram_received(self, data, addr):
        """Handle received broadcast message."""
        try:
            if data[:4] == b"\x00\x00\x66\x99":
                # 6699 format (protocol 3.5, port 7000)
                decoded = json.loads(decrypt_6699(data))
            else:
                # 55AA format (ports 6666/6667)
                data = data[20:-8]
                try:
                    data = decrypt_udp(data)
                except Exception:  # pylint: disable=broad-except
                    data = data.decode()
                decoded = json.loads(data)
            self.device_found(decoded)
        except Exception:  # pylint: disable=broad-except
            _LOGGER.debug("Failed to decode discovery message from %s", addr)

    def device_found(self, device):
        """Discover a new device."""
        if device.get("gwId") not in self.devices:
            self.devices[device.get("gwId")] = device
            _LOGGER.debug("Discovered device: %s", device)

        if self._callback:
            self._callback(device)


async def discover():
    """Discover and return devices on local network."""
    discovery = TuyaDiscovery()
    try:
        await discovery.start()
        await asyncio.sleep(DEFAULT_TIMEOUT)
    finally:
        discovery.close()
    return discovery.devices
