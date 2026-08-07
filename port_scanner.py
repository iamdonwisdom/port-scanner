from scanner import start_scan


def main():
    print("=" * 60)
    print("        PYTHON PORT SCANNER v2.0")
    print("=" * 60)

    target = input("\nEnter Target IP or Domain: ")

    print("\nChoose Scan Mode")
    print("1. Quick Scan (Top 30 Common Ports)")
    print("2. Full Scan (1 - 65535)")
    print("3. Custom Port Range")

    choice = input("\nEnter Choice: ")

    if choice == "1":
        start_scan(target, mode="quick")

    elif choice == "2":
        start_scan(target, mode="full")

    elif choice == "3":
        start_port = int(input("Starting Port: "))
        end_port = int(input("Ending Port: "))
        start_scan(target, mode="custom",
                   start_port=start_port,
                   end_port=end_port)

    else:
        print("Invalid option selected.")


if __name__ == "__main__":
    main()
