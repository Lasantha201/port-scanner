# Script written by deepcoder

import sys
import socket
from datetime import datetime


# Define color (green text) and reset

COLOR = "\033[0;32m"  # Green color
RESET = "\033[0m"     # Reset color to default


def main():
    # Use the color for all the user inputs

    target = input(f"{COLOR}Enter IP or Domain address: {RESET}")
    start_port = int(input(f"{COLOR}Enter starting port: {RESET}"))
    end_port = int(input(f"{COLOR}Enter ending port: {RESET}"))

    print("\n")

    # Banner with colored text (Green)

    print(f"{COLOR}-" * 50)
    print(f"{COLOR}Scanning target {target} from port {start_port} to {end_port}")
    print(f"{COLOR}Time started: {datetime.now()}")
    print(f"{COLOR}-" * 50)

    print("\n")

    # Process for searching open ports

    try:

        for port in range(start_port, end_port):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            result = s.connect_ex((target, port))

            if result == 0:
                print(f"{COLOR}Port {port} open.{RESET}")  # print open port
            s.close()

    except KeyboardInterrupt:
        print(f"\n{COLOR}Exiting program!{RESET}")
        sys.exit()

    except socket.gaierror:
        print(f"{COLOR}Hostname could not be resolved!{RESET}")
        sys.exit()

    except socket.error:
        print(f"{COLOR}Could not connect to the server!{RESET}")
        sys.exit()


if __name__ == "__main__":
    main()
