from scapy.all import sniff, IP
from detector import process_packet

def packet_callback(packet):
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        process_packet(src_ip)

def start_sniffer():
    sniff(filter="ip", prn=packet_callback, store=0)
