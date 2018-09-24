from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor


# UDP Protocol
class EchoUDP(DatagramProtocol):

    def datagramReceived(self, datagram, address):
        print ("received {} from {}".format(datagram, address))
        self.transport.write(datagram, address)


def main():
    reactor.listenUDP(8000, EchoUDP())
    reactor.run()


if __name__ == '__main__':
    main()