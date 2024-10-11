import can


def test_can_device(bus):
    try:
        msg = can.Message(arbitration_id=0x426, is_remote_frame=True, is_extended_id=False)
        bus.send(msg)
        print("Test message sent. Waiting for a response...")
        response = bus.recv(timeout=1.0)  # Wait for 1 second
        if response:
            print(f"Received response: {response}")
        else:
            print("No response received.")
    except can.CanError as e:
        print(f"CAN device test failed: {e}")


    finally:
        # Properly shutdown the bus after use
        bus.shutdown()


# Example usage
bus = can.interface.Bus(interface='socketcan', channel='can0', bitrate=100000)
test_can_device(bus)
