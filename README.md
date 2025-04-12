A network sniffer (also known as a packet sniffer or network analyzer) is a tool used to capture, inspect, and analyze network traffic flowing over a computer network.

🔍 Description of a Network Sniffer:
Function:
It intercepts and logs data packets traveling across the network. This includes both incoming and outgoing packets.

Usage:
Network troubleshooting
Monitoring network usage
Detecting malicious activity
Penetration testing
Protocol analysis

How it works:
A network interface card (NIC) normally discards all traffic not addressed to it. A sniffer puts the NIC into promiscuous mode, so it captures all packets on the local network segment.


## Getting Started

### Running the Tool
1. Open command prompt as administrator
2. Navigate to the project directory
3. Run the command:
## Getting Started

### Basic Controls
- Start capture: Automatic upon launch
- Stop capture: Press `Ctrl+C`

## Features

### Packet Capture
- Real-time network traffic monitoring
- Captures both incoming and outgoing packets
- Supports multiple protocols (TCP, UDP)

### Display Information
- Timestamp
- Source IP and Port
- Destination IP and Port
- Protocol type
- Packet length
- TCP flags (for TCP packets)

## Usage

### Reading the Output
Example output:

Components:
- Timestamp: When the packet was captured
- Source: Origin IP and port
- Destination: Target IP and port
- Protocol: Network protocol used
- Length: Size of the packet
- Flags: TCP flags (if applicable)

### Color Coding
- Yellow: Timestamp
- Green: Source information
- Red: Destination information
- Blue: Protocol type

## Troubleshooting

### Common Issues

1. **Permission Denied**
   - Solution: Run the program as administrator

2. **No Packets Captured**
   - Check network interface connection
   - Verify administrator privileges
   - Ensure antivirus isn't blocking the tool

3. **Installation Errors**
   - Verify Python version
   - Try reinstalling dependencies
   - Check for system compatibility

## Legal Considerations

### Important Notes
- Only use on networks you own or have explicit permission to monitor
- Network sniffing without authorization may be illegal
- Respect privacy and data protection laws
- For educational and administrative purposes only

### Best Practices
- Obtain necessary permissions before use
- Document your monitoring activities
- Handle captured data securely
- Follow organizational security policies

## Support
For technical issues or questions:
- Check documentation
- Review code comments
- Consult with network administrator
