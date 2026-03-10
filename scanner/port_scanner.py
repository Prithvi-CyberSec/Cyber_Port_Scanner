import socket
from concurrent.futures import ThreadPoolExecutor
from .services import get_service

class PortScanner:

    def __init__(self, target, start_port, end_port):
        self.target = socket.gethostbyname(target)
        self.start_port = start_port
        self.end_port = end_port

    def scan_port(self, port):

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)

        result = s.connect_ex((self.target, port))

        if result == 0:
            service = get_service(port)
            print(f"Port {port} -> OPEN ({service})")

        s.close()

    def scan(self):

        print(f"Scanning {self.target}...\n")

        with ThreadPoolExecutor(max_workers=100) as executor:
            executor.map(self.scan_port, range(self.start_port, self.end_port))

        print("\nScan complete.")
