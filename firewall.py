import subprocess

blocked_ips = set()

def block_ip(ip):
    if ip in blocked_ips:
        return

    rule_name = f"Block_Attacker_{ip}"
    command = [
        "netsh", "advfirewall", "firewall", "add", "rule",
        f"name={rule_name}", "dir=in", "action=block", f"remoteip={ip}"
    ]
    try:
        subprocess.run(command, check=True)
        print(f"[✔] Firewall rule added: {ip} has been blocked.")
        blocked_ips.add(ip)
    except subprocess.CalledProcessError:
        print(f"[ERROR] Failed to block IP: {ip}")
