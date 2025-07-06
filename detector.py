from collections import defaultdict
from time import time
from ipaddress import ip_address, ip_network
from geo_lookup import get_ip_location
from logger import log_attack
from config import DETECTION_WINDOW, FLOOD_THRESHOLD, SAFE_IPS_FILE
from firewall import block_ip, is_ip_blocked
from popup_alert import show_block_popup

packet_log = defaultdict(list)
safe_networks = []

def load_safe_ips():
    global safe_networks
    try:
        with open(SAFE_IPS_FILE) as f:
            lines = [line.strip() for line in f if line.strip()]
            safe_networks = [ip_network(ip) for ip in lines]
    except FileNotFoundError:
        safe_networks = []

def is_safe(ip):
    ip_obj = ip_address(ip)
    return any(ip_obj in net for net in safe_networks)

load_safe_ips()

def process_packet(ip):
    if is_safe(ip):
        return
    if is_ip_blocked(ip):
        return

    now = time()
    packet_log[ip] = [t for t in packet_log[ip] if now - t < DETECTION_WINDOW]
    packet_log[ip].append(now)

    if len(packet_log[ip]) > FLOOD_THRESHOLD:
        location = get_ip_location(ip)
        print(f"[!] Flood Detected: {ip} from {location}")
        log_attack(ip, location)
        block_ip(ip)
        show_block_popup(ip, location)
        packet_log[ip].clear()
