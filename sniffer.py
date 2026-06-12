from scapy.all import sniff

def packet_callback(packet):
    print("\nPacket Captured:")
    print(packet.summary())

print("Starting Packet Capture...")
sniff(count=10, prn=packet_callback)

print("\nCapture Completed.")
