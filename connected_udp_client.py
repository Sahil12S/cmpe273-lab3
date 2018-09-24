from __future__ import print_function

import sys, time

from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

class ClientDatagram(DatagramProtocol):

    def startProtocol(self):
        host = "127.0.0.1"
        port = 8000

        self.transport.connect(host, port)
        print("now we can only send to host {} and port {}".format(host, port))
        self.sendDatagram()

    
    def sendDatagram(self):
        message = "Hello World!"
        datagram = message.encode()
        self.transport.write(datagram)


    def datagramReceived(self, datagram, host):
        print("datagram received {}".format(repr(datagram)))

    
    def connectionRefused(self):
        print("no one is listening")


def main():
    protocol = ClientDatagram()
    t = reactor.listenUDP(0, protocol)
    reactor.run()


if __name__ == '__main__':
    main()