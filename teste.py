import time

from digi.xbee.models.status import NetworkDiscoveryStatus
from digi.xbee.devices import XBeeDevice
from digi.xbee.devices import ZigBeeDevice
from digi.xbee.devices import RemoteXBeeDevice
from digi.xbee.devices import XBee64BitAddress

# TODO: Replace with the serial port where your local module is connected to.
PORT = "COM6"
# TODO: Replace with the baud rate of your local module.
BAUD_RATE = 9600


def main():
    print(" +---------------------------------------------+")
    print(" | XBee Python Library Discover Devices Sample |")
    print(" +---------------------------------------------+\n")

    device = XBeeDevice(PORT, BAUD_RATE)
    #device = ZigBeeDevice(PORT, BAUD_RATE)
    xbee = XBeeDevice(PORT, BAUD_RATE)
    remote = RemoteXBeeDevice(xbee, XBee64BitAddress.from_hex_string("0013A20041AEB3D3"))

    try:
        device.open()
        xbee.open()
        #rotas = device._get_routes(route_cb=None, finished_cb=None, timeout=None)
        #print(rotas)
        
        rotas = device.get_route_to_node(remote=any, timeout=10, force=True)
        print(rotas)

        #remote.read_device_info()

        

        xbee_network = device.get_network()

        xbee_network.set_discovery_timeout(15)  # 15 seconds.

        xbee_network.clear()


        # Callback for discovered devices.
        def callback_device_discovered(remote):
            print("Device discovered: %s" % remote)

        
        # Callback for discovery finished.
        def callback_discovery_finished(status):
            if status == NetworkDiscoveryStatus.SUCCESS:
                print("Discovery process finished successfully.")
            else:
                print("There was an error discovering devices: %s" % status.description)

        xbee_network.add_device_discovered_callback(callback_device_discovered)

        xbee_network.add_discovery_process_finished_callback(callback_discovery_finished)

        xbee_network.start_discovery_process()

        print("Discovering remote XBee devices...")

        while xbee_network.is_discovery_running():
            time.sleep(0.1)

    finally:
        if device is not None and device.is_open():
            device.close()


if __name__ == '__main__':
    main()