from collections import defaultdict
from time import time
from geo_lookup import get_ip_location
from logger import log_attack
from config import DETECTION_WINDOW, FLOOD_THRESHOLD

packet_log = defaultdict(list)

def process_packet(ip):
    now = time()
    packet_log[ip] = [t for t in packet_log[ip] if now - t < DETECTION_WINDOW]
    packet_log[ip].append(now)

    if len(packet_log[ip]) > FLOOD_THRESHOLD:
        location = get_ip_location(ip)
        print(f"[!] Flood Detected: {ip} from {location}")
        log_attack(ip, location)
        packet_log[ip].clear()
