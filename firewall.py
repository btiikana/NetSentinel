import subprocess

def block_ip(ip):
    rule_name = f"Block_Attacker_{ip}"
    command = [
        "netsh", "advfirewall", "firewall", "add", "rule",
        f"name={rule_name}", "dir=in", "action=block", f"remoteip={ip}"
    ]
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError:
        print(f"[ERROR] Failed to block IP: {ip}")
