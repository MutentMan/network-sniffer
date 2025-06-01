const chalk = require('chalk');

class PacketAnalyzer {
  analyzePacket(packet) {
    if (!packet.payload?.payload) return null;

    const ip = packet.payload.payload;
    const timestamp = new Date().toISOString();
    
    const packetInfo = {
      timestamp,
      sourceIp: ip.saddr.toString(),
      destIp: ip.daddr.toString(),
      protocol: ip.protocol,
      length: packet.pcap_header.len
    };

    if (ip.payload) {
      packetInfo.sourcePort = ip.payload.sport;
      packetInfo.destPort = ip.payload.dport;
      
      if (ip.payload.flags) {
        packetInfo.flags = ip.payload.flags;
      }
    }

    return packetInfo;
  }

  formatPacketInfo(packetInfo) {
    if (!packetInfo) return '';

    const protocolMap = {
      6: 'TCP',
      17: 'UDP'
    };

    const protocol = protocolMap[packetInfo.protocol] || packetInfo.protocol;
    
    let output = [
      chalk.yellow(packetInfo.timestamp),
      '|',
      chalk.green(`${packetInfo.sourceIp}:${packetInfo.sourcePort || '?'}`),
      '→',
      chalk.red(`${packetInfo.destIp}:${packetInfo.destPort || '?'}`),
      '|',
      chalk.blue(protocol),
      '|',
      `Length: ${packetInfo.length} bytes`
    ];

    if (packetInfo.flags) {
      output.push(`| Flags: ${packetInfo.flags}`);
    }

    return output.join(' ');
  }
}

module.exports = { PacketAnalyzer };