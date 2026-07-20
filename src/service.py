#!/usr/bin/env python3

import meshtastic.serial_interface
from pubsub import pub


def on_receive(packet, interface):
    decoded = packet.get("decoded", {})
    portnum = decoded.get("portnum", "UNKNOWN")

    print(
        f"RX {portnum} "
        f"from={packet.get('fromId')} "
        f"RSSI={packet.get('rxRssi')} "
        f"SNR={packet.get('rxSnr')}"
    )


def on_connection(interface):
    print("Connected")


pub.subscribe(on_receive, "meshtastic.receive")
pub.subscribe(on_connection, "meshtastic.connection.established")


interface = meshtastic.serial_interface.SerialInterface(
    devPath="/dev/ttyACM0"
)

print("Listening...")

try:
    while True:
        pass
except KeyboardInterrupt:
    interface.close()