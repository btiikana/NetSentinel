import csv
from datetime import datetime

LOG_FILE = "logs/attack_log.csv"

def log_attack(ip, location):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    row = [timestamp, ip, location]
    print(f"[LOGGED] {timestamp} | {ip} | {location}")
    
    with open(LOG_FILE, mode='a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(row)
