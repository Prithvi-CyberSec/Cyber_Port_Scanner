import sys
from scanner.port_scanner import PortScanner

if len(sys.argv) < 2:
    print("Usage: python main.py <target> [start_port] [end_port]")
    sys.exit()

target = sys.argv[1]

start_port = int(sys.argv[2]) if len(sys.argv) > 2 else 1
end_port = int(sys.argv[3]) if len(sys.argv) > 3 else 1024

scanner = PortScanner(target, start_port, end_port)
scanner.scan()
