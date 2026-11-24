#!/usr/bin/env python3
"""Simple cross-platform ping script using Python's standard library."""

import argparse
import platform
import subprocess
import sys


def ping(host: str, count: int = 4, timeout: int = 2) -> bool:
    """Ping a host and return True if reachable, False otherwise."""
    system = platform.system().lower()

    if system == "windows":
        cmd = ["ping", "-n", str(count), "-w", str(timeout * 1000), host]
    elif system == "darwin":
        # On macOS, -W specifies timeout in milliseconds
        cmd = ["ping", "-c", str(count), "-W", str(timeout * 1000), host]
    else:
        # On Linux, -W specifies timeout in seconds
        cmd = ["ping", "-c", str(count), "-W", str(timeout), host]

    try:
        result = subprocess.run(cmd, check=False)
        return result.returncode == 0
    except FileNotFoundError:
        print("Error: 'ping' command not found on this system.", file=sys.stderr)
        return False


def main() -> int:
    parser = argparse.ArgumentParser(description="Simple Python ping script.")
    parser.add_argument("host", nargs="?", help="Hostname or IP address to ping")
    parser.add_argument(
        "-c",
        "--count",
        type=int,
        default=4,
        help="Number of ping packets to send (default: 4)",
    )
    parser.add_argument(
        "-t",
        "--timeout",
        type=int,
        default=2,
        help="Timeout per packet in seconds (default: 2)",
    )
    args = parser.parse_args()

    host = args.host
    if not host:
        try:
            host = input("Host oder IP eingeben: ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return 1

    if not host:
        print("Kein Host angegeben.", file=sys.stderr)
        return 1

    reachable = ping(host, count=args.count, timeout=args.timeout)
    if reachable:
        print(f"\n✓ {host} ist erreichbar.")
        return 0

    print(f"\n✗ {host} ist nicht erreichbar.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
