from packet_sniffer import start_sniffer
from geo_lookup import close_reader

print("🚨 NetSentinel: Real-time Intrusion Monitor Started")

try:
    start_sniffer()
except KeyboardInterrupt:
    print("🛑 NetSentinel stopped by user.")
finally:
    close_reader()
