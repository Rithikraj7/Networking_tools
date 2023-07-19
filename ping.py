import os
import platform
import time
import subprocess

def ping(host):
    ping_command = ["ping", "-n" if platform.system().lower() == "windows" else "-c", "4", host]
    try:
        output = subprocess.check_output(ping_command, stderr=subprocess.STDOUT, universal_newlines=True)
        return output
    except subprocess.CalledProcessError as e:
        return e.output

if __name__ == "__main__":
    target_host = input("Enter the IP address or domain name to ping: ")

    print(f"Pinging {target_host}...")

    start_time = time.time()
    result = ping(target_host)
    end_time = time.time()

    if "Request timed out" in result:
        print("Ping request timed out.")
    else:
        print(result)

    print(f"Ping completed in {end_time - start_time:.2f} seconds.")
