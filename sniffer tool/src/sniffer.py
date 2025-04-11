from scapy.all import sniff, IP, TCP, UDP
from datetime import datetime
import threading
import queue

class NetworkSniffer:
    def __init__(self):
        self.packet_queue = queue.Queue()
        self.is_running = False
        self.capture_thread = None

    def packet_callback(self, packet):
        if packet.haslayer(IP):
            self.packet_queue.put(packet)

    def start_capture(self, interface=None, filter=""):
        """
        Start capturing packets on the specified interface
        :param interface: Network interface to capture on (None for default)
        :param filter: BPF filter string
        """
        self.is_running = True
        self.capture_thread = threading.Thread(
            target=self._capture_packets,
            args=(interface, filter)
        )
        self.capture_thread.start()

    def _capture_packets(self, interface, filter):
        try:
            sniff(
                iface=interface,
                filter=filter,
                prn=self.packet_callback,
                store=False,
                stop_filter=lambda _: not self.is_running
            )
        except Exception as e:
            print(f"Error during packet capture: {e}")

    def stop_capture(self):
        """Stop the packet capture"""
        self.is_running = False
        if self.capture_thread:
            self.capture_thread.join()

    def get_packet(self):
        """Get the next packet from the queue"""
        try:
            return self.packet_queue.get_nowait()
        except queue.Empty:
            return None