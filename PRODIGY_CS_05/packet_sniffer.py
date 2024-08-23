from scapy.all import sniff, IP, TCP, UDP, Raw

def packet_callback(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        proto = packet[IP].proto
        
        if packet.haslayer(TCP):
            proto = 'TCP'
            payload = packet[TCP].payload
        elif packet.haslayer(UDP):
            proto = 'UDP'
            payload = packet[UDP].payload
        else:
            proto = 'Unknown'
            payload = b''

        # Print packet details
        print(f"Source IP: {ip_src}")
        print(f"Destination IP: {ip_dst}")
        print(f"Protocol: {proto}")
        if payload:
            print(f"Payload: {payload}")
        print("-" * 40)

def start_sniffer(interface=None):
    print("Starting packet sniffer...")
    # Capture packets on the specified interface (or all interfaces if None)
    sniff(iface=interface, prn=packet_callback, store=0)

if __name__ == "__main__":
    interface = input("Enter the network interface to sniff (or press Enter to sniff all interfaces): ")
    start_sniffer(interface if interface else None)
