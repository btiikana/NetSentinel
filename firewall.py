import subprocess

def block_ip(ip):
    """Blocks the given IP using Windows Firewall."""
    if is_ip_blocked(ip):
        return  # Already blocked, skip

    rule_name = f"Block_Attacker_{ip}"
    command = [
        "netsh", "advfirewall", "firewall", "add", "rule",
        f"name={rule_name}", "dir=in", "action=block", f"remoteip={ip}"
    ]
    try:
        subprocess.run(command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"[✔] Firewall rule added: {ip} has been blocked.")
    except subprocess.CalledProcessError:
        print(f"[ERROR] Failed to block IP: {ip}")

def is_ip_blocked(ip):
    """Checks if the IP is already blocked by the firewall."""
    rule_name = f"Block_Attacker_{ip}"
    result = subprocess.run(
        ["netsh", "advfirewall", "firewall", "show", "rule", f"name={rule_name}"],
        capture_output=True,
        text=True
    )
    return rule_name in result.stdout
