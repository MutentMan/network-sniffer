from scapy.all import IP, TCP, UDP
from colorama import Fore, Style
from datetime import datetime

class PacketAnalyzer:
    @staticmethod
    def analyze_packet(packet):
        if not packet.haslayer(IP):
            return None

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        ip_packet = packet[IP]
        
        # Basic packet info
        packet_info = {
            "timestamp": timestamp,
            "source_ip": ip_packet.src,
            "dest_ip": ip_packet.dst,
            "protocol": ip_packet.proto,
            "length": len(packet),
        }

        # Add TCP-specific info
        if packet.haslayer(TCP):
            tcp = packet[TCP]
            packet_info.update({
                "source_port": tcp.sport,
                "dest_port": tcp.dport,
                "flags": tcp.flags
            })
        
        # Add UDP-specific info
        elif packet.haslayer(UDP):
            udp = packet[UDP]
            packet_info.update({
                "source_port": udp.sport,
                "dest_port": udp.dport
            })

        return packet_info

    @staticmethod
    def format_packet_info(packet_info):
        if not packet_info:
            return ""

        protocol_map = {6: "TCP", 17: "UDP"}
        protocol = protocol_map.get(packet_info["protocol"], str(packet_info["protocol"]))
        
        output = (
            f"{Fore.YELLOW}{packet_info['timestamp']}{Style.RESET_ALL} | "
            f"{Fore.GREEN}{packet_info['source_ip']}:{packet_info.get('source_port', '?')}{Style.RESET_ALL} → "
            f"{Fore.RED}{packet_info['dest_ip']}:{packet_info.get('dest_port', '?')}{Style.RESET_ALL} | "
            f"{Fore.BLUE}{protocol}{Style.RESET_ALL} | "
            f"Length: {packet_info['length']} bytes"
        )

        if "flags" in packet_info:
            output += f" | Flags: {packet_info['flags']}"

        return output