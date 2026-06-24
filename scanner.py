# VulnProbe - Network Vulnerability Scanner
# Stage 1: Port Scanner with Service Detection
# Author: Adithya9x

import socket
import datetime

def resolve_target(target):
    try:
        ip = socket.gethostbyname(target)
        return ip
    except:
        print("[-] Invalid target. Could not resolve hostname.")
        exit()

def get_service(port):
    try:
        service = socket.getservbyport(port)
        return service
    except:
        return "Unknown Service"

def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        sock.close()
        if result == 0:
            return True
        else:
            return False
    except:
        return False

def run_scanner(target, start_port, end_port):
    ip = resolve_target(target)

    print("-" * 50)
    print(f"  VulnProbe - Network Vulnerability Scanner")
    print(f"  Target   : {target} ({ip})")
    print(f"  Ports    : {start_port} to {end_port}")
    print(f"  Started  : {datetime.datetime.now()}")
    print("-" * 50)

    open_ports = []

    for port in range(start_port, end_port + 1):
        print(f"  Scanning port {port}...", end="\r")
        if scan_port(ip, port):
            service = get_service(port)
            print(f"  [OPEN] Port {port:5} --> {service:20}")
            open_ports.append((port, service))

    print("-" * 50)
    print(f"  Scan complete. {len(open_ports)} open port(s) found.")
    print("-" * 50)
    return open_ports

target = input("Enter target IP or hostname: ")
start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))

run_scanner(target, start_port, end_port)