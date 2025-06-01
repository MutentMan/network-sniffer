import sys
import time
from src.sniffer import NetworkSniffer
from src.packet_analyzer import PacketAnalyzer
from colorama import init

def main():
    # Initialize colorama for Windows color support
    init()

    # Create sniffer instance
    sniffer = NetworkSniffer()
    analyzer = PacketAnalyzer()

    print("Starting packet capture... Press Ctrl+C to stop")
    
    try:
        # Start capturing packets
        sniffer.start_capture()

        while True:
            # Get and analyze packets
            packet = sniffer.get_packet()
            if packet:
                packet_info = analyzer.analyze_packet(packet)
                if packet_info:
                    print(analyzer.format_packet_info(packet_info))
            time.sleep(0.001)  # Small delay to prevent CPU overuse

    except KeyboardInterrupt:
        print("\nStopping packet capture...")
    finally:
        sniffer.stop_capture()

if __name__ == "__main__":
    # Check for administrator privileges
    if sys.platform.startswith('win32'):
        import ctypes
        if not ctypes.windll.shell32.IsUserAnAdmin():
            print("This program requires administrator privileges.")
            print("Please run as administrator.")
            sys.exit(1)
    
    main()