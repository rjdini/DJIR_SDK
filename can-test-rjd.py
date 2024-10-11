import can


def send_can_message():
    try:
        # Create a bus object using the "interface" argument
        bus = can.interface.Bus(channel='can0', interface='socketcan')

        # Create a message object
        msg = can.Message(arbitration_id=0x123, data=[0x01, 0x02, 0x03, 0x04], is_extended_id=False)

        # Send the message on the bus
        bus.send(msg)

        print(f"Message sent on {bus.channel_info}")

    except can.CanError as e:
        print(f"CAN error: {e}")

    finally:
        # Properly shutdown the bus after use
        bus.shutdown()


def receive_can_message():
    try:
        # Create a bus object using the "interface" argument
        bus = can.interface.Bus(channel='can0', interface='socketcan')

        print("Listening for CAN messages...")
        # Listen for a message on the bus
        msg = bus.recv(timeout=10.0)  # Timeout in seconds

        if msg:
            print(f"Received message: {msg}")
        else:
            print("No message received within timeout")

    except can.CanError as e:
        print(f"CAN error: {e}")

    finally:
        # Properly shutdown the bus after use
        bus.shutdown()


if __name__ == "__main__":
    send_can_message()  # To send a message
    receive_can_message()  # To receive a message
