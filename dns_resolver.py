import socket


def dns_resolver(domain_name):
    try:
        ip_address = socket.gethostbyname(domain_name)
        return ip_address
    except socket.gaierror as e:
        return None


if __name__ == "__main__":
    domain_name = input("Enter a domain name to resolve: ")
    ip_address = dns_resolver(domain_name)

    if ip_address:
        print(f"The IP address of {domain_name} is {ip_address}")
    else:
        print(f"Failed to resolve {domain_name}. Please check the domain name.")
