const pcap = require('pcap');
const EventEmitter = require('events');

class NetworkSniffer extends EventEmitter {
  constructor() {
    super();
    this.session = null;
  }

  startCapture(interface, filter = '') {
    return new Promise((resolve, reject) => {
      try {
        this.session = pcap.createSession(interface, filter);
        
        this.session.on('packet', (raw_packet) => {
          const packet = pcap.decode.packet(raw_packet);
          this.emit('packet', packet);
        });

        resolve();
      } catch (error) {
        reject(error);
      }
    });
  }

  stopCapture() {
    if (this.session) {
      this.session.close();
      this.session = null;
    }
  }
}

module.exports = { NetworkSniffer };