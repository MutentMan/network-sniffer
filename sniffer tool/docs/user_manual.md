# Network Sniffer Tool - User Manual

## Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Getting Started](#getting-started)
4. [Features](#features)
5. [Usage](#usage)
6. [Troubleshooting](#troubleshooting)
7. [Legal Considerations](#legal-considerations)

## Introduction
The Network Sniffer Tool is a Python-based application for capturing and analyzing network traffic in real-time. It provides network administrators, security researchers, and developers with insights into network communications.

## Installation

### Prerequisites
- Python 3.7 or higher
- Administrator privileges
- Windows operating system

### Setup Steps
1. Clone or download the project
2. Open command prompt as administrator
3. Navigate to the project directory
4. Install dependencies:

5. 
## Getting Started

### Running the Tool
1. Open command prompt as administrator
2. Navigate to the project directory
3. Run the command:


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
