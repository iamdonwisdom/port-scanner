import socket

# Common ports and services
services = {
    21: "FTP",
    22: "SSH",
    23: "TELNET",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS"
}

target = input("Enter target IP or domain: ")

print(f"\nScanning {target}...\n")

for port in range(1, 1025):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    result = s.connect_ex((target, port))

    if result == 0:
        service = services.get(port, "Unknown")
        print(f"[+] Port {port} is OPEN ({service})")

    s.close()

print("\nScan completed.")

