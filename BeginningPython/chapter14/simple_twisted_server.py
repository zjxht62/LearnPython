from twisted.internet import reactor
from twisted.internet.protocol import Protocol, Factory

# 自定义协议继承Protocol类
class SimpleLogger(Protocol):
    def connectionMade(self):
        print('Got connection from', self.transport.client)

    def connectionLost(self, reason):
        print(self.transport.client, 'disconnected')

    def dataReceived(self, data):
        print(data)

# 实例化Factory，并设置Protocol属性
factory = Factory()
factory.protocol = SimpleLogger

# factory负责在新连接来到的时候创建协议对象
reactor.listenTCP(1234, factory)
reactor.run()

