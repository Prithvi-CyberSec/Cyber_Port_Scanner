# Cyber_Port_Scanner
A fast and simple TCP port scanner that checks open ports on a target host.


# Port Scanner 🔎

A fast and simple multithreaded port scanner written in Python.

## Features

* Scan single port or port ranges
* Multithreaded scanning for speed
* Domain name resolution
* Basic service detection
* Clean CLI output

## Installation

```bash
git clone https://github.com/yourusername/port-scanner.git
cd port-scanner
pip install -r requirements.txt
```

## Usage

Scan common ports:

```bash
python main.py example.com
```

Scan specific range:

```bash
python main.py example.com 1 1024
```

## Example Output

```
Scanning target: example.com

Port 22  -> OPEN (SSH)
Port 80  -> OPEN (HTTP)
Port 443 -> OPEN (HTTPS)

Scan Complete
```

## Project Structure

```
scanner/
    port_scanner.py -> scanning engine
    utils.py        -> networking utilities
    services.py     -> port service mappings
```

## Legal Notice

This tool is for educational purposes only. Do not scan systems without permission.

## License

MIT License
