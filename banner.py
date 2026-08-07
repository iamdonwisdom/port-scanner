import socket

def grab_banner(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        sock.connect((target, port))

        if port in [80, 8080, 8000]:
            sock.send(b"HEAD / HTTP/1.0\r\n\r\n")

        elif port == 443:
            return "HTTPS Service"

        elif port == 22:
            pass

        banner = sock.recv(1024).decode(errors="ignore").strip()

        sock.close()

        if banner:
            return banner

    except:
        pass

    return "No Banner"
