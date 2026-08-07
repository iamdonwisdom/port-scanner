from datetime import datetime
import os

def save_report(target, results):
    os.makedirs("reports", exist_ok=True)

    filename = f"reports/scan_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

    with open(filename, "w") as f:
        f.write(f"Port Scan Report\n")
        f.write(f"Target: {target}\n\n")

        for port, service in results:
            f.write(f"Port {port} OPEN ({service})\n")

    print(f"\nReport saved: {filename}")
