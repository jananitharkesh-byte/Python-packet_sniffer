from scapy.all import sniff, IP, TCP, UDP, ICMP

def analyze_packet(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto

        print("\n--- Packet Captured ---")
        print(f"Source IP: {src_ip}")
        print(f"Destination IP: {dst_ip}")

        if TCP in packet:
            sport = packet[TCP].sport
            dport = packet[TCP].dport

            print("Protocol: TCP")
            print(f"Source Port: {sport}")
            print(f"Destination Port: {dport}")

            if sport == 80 or dport == 80:
                print("Service: HTTP")
            elif sport == 443 or dport == 443:
                print("Service: HTTPS")

        elif UDP in packet:
            sport = packet[UDP].sport
            dport = packet[UDP].dport

            print("Protocol: UDP")
            print(f"Source Port: {sport}")
            print(f"Destination Port: {dport}")

            if sport == 443 or dport == 443:
                print("Service: HTTPS (QUIC)")

        elif ICMP in packet:
            print("Protocol: ICMP")

        else:
            print(f"Protocol Number: {protocol}")

print("Starting packet sniffer... capturing packets for 30 seconds.")
sniff(prn=analyze_packet, store=False, timeout=30)