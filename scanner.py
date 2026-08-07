from banner import grab_banner
from report import save_report
import socket
import time
from concurrent.futures import ThreadPoolExecutor

COMMON_PORTS = {
    20: "FTP Data",
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    123: "NTP",
    135: "MS RPC",
    139: "NetBIOS",
    143: "IMAP",
    161: "SNMP",
    389: "LDAP",
    443: "HTTPS",
    445: "SMB",
    465: "SMTPS",
    587: "SMTP Submission",
    993: "IMAPS",
    995: "POP3S",
    1433: "Microsoft SQL Server",
    1521: "Oracle",
    2049: "NFS",
    3306: "MySQL",
    3389: "Remote Desktop",
    5432: "PostgreSQL",
    5900: "VNC",
    6379: "Redis",
    8080: "HTTP Alternate",
    8443: "HTTPS Alternate"
}


def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)

        if sock.connect_ex((target, port)) == 0:
            service = COMMON_PORTS.get(port, "Unknown")
            banner = grab_banner(target, port)
            sock.close()
            return (port, service, banner)

        sock.close()

    except Exception:
        pass

    return None


def start_scan(target, mode, start_port=None, end_port=None):

    print("\nResolving target...")

    try:
        ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("Unable to resolve target.")
        return

    print(f"Target IP: {ip}")

    if mode == "quick":
        ports = list(COMMON_PORTS.keys())

    elif mode == "top1000":
        ports = range(1, 1001)

    elif mode == "full":
        ports = range(1, 65536)

    elif mode == "custom":
        ports = range(start_port, end_port + 1)

    else:
        print("Invalid mode.")
        return

    print("\nStarting scan...\n")

    start_time = time.time()

    results = []

    with ThreadPoolExecutor(max_workers=500) as executor:

        for result in executor.map(lambda p: scan_port(ip, p), ports):

            if result:

                port, service, banner = result

                print(f"[OPEN] Port {port:<6} {service:<20} {banner}")

                results.append((port, service))

    end_time = time.time()

    save_report(ip, results)

    print("\n" + "=" * 55)
    print("Scan Completed Successfully")
    print(f"Open Ports   : {len(results)}")
    print(f"Elapsed Time : {end_time-start_time:.2f} seconds")
    print("=" * 55)
