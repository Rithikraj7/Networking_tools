import socket

def scan_ports(target, ports):
    open_ports = []
    for port in ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)  # Set a timeout for the connection attempt
                result = s.connect_ex((target, port))
                if result == 0:
                    open_ports.append(port)
        except socket.error:
            pass
    return open_ports

if __name__ == "__main__":
    target_host = input("Enter the target host to scan (e.g., example.com or 192.168.0.1): ")
    port_range = input("Enter the port range to scan (e.g., 1-100): ")

    start_port, end_port = map(int, port_range.split('-'))
    ports_to_scan = range(start_port, end_port + 1)

    open_ports = scan_ports(target_host, ports_to_scan)

    if open_ports:
        print(f"Open ports on {target_host}: {', '.join(map(str, open_ports))}")
    else:
        print(f"No open ports found on {target_host}.")


# Enter the target host to scan (e.g., example.com or 192.168.0.1): google.com
# Enter the port range to scan (e.g., 1-100): 1-1024
# Open ports on google.com: 80, 443

