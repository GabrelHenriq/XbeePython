import time

from digi.xbee.models.status import NetworkDiscoveryStatus
from digi.xbee.devices import XBeeDevice
from digi.xbee.devices import ZigBeeDevice
from digi.xbee.devices import RemoteXBeeDevice
from digi.xbee.models.address import XBee64BitAddress


# TODO: Replace with the serial port where your local module is connected to.
PORT = "COM6"
# TODO: Replace with the baud rate of your local module.
BAUD_RATE = 9600



print(" +---------------------------------------------+")
print(" | XBee Python Library Discover Devices Sample |")
print(" +---------------------------------------------+\n")

#device = XBeeDevice(PORT, BAUD_RATE)
#device = ZigBeeDevice(PORT, BAUD_RATE)
xbee = XBeeDevice(PORT, BAUD_RATE)

xbee.open()

remote = RemoteXBeeDevice(xbee, XBee64BitAddress.from_hex_string("0013A20041AEB242"))

xbee.close()
#device.open()

remote.read_device_info()
