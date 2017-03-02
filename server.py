import daemon
import struct
import socket
import socketserver
from importlib import import_module as loader
import common

class Request_Handler(socketserver.BaseRequestHandler):
    def handle(self):
        while True: #如果退出循环或发生异常，系统底层会自动关闭socket连接
            header = self.request.recv(common.WASHER_HEADER_LENGTH)
            (body_length, api, protocol, num, sys) = struct.unpack('>5I', header)
            print('body_length:{} api:{} protocol:{} num:{} sys:{}'.format(body_length, api, protocol, num, sys))
            body = self.request.recv(body_length)
            _router(self.request, api, protocol, sys, body)

class Washer_Server(socketserver.ThreadingMixIn, socketserver.TCPServer):
    def verify_request(self, request, client_address):
        return True
    
    #关闭服务器的时调用此方法做数据善后处理
    def server_close(self):
        self.shutdown()
        self.socket.close()

    def handle_timeout(self):
        pass

    def handle_error(self, request,  client_address):
        """
        如果Request_Handler发生异常会调用此方法
        如果Reqeust_Handler发生异常，会关闭socket连接,底层会调用shutdown_request()方法
        如有异常可以在里做一些数据清理，保存
        """
        print("client socket close..")
        #socketserver.TCPServer.handle_error(self, request, client_address)
        super(Washer_Server, self).handle_error(request, client_address)

def _router(socket, api, protocol, sys, data):
    """ 业务路由 """
    api = 'api.v' + str(api)
    index = str(protocol)[:2]
    model = common.MOD.get(index) #根据协议前两位获取对应模块

    if model is None:
        print('model:{} not found'.format(index))
        return
    model = loader(api + '.' + model)
    model.handle(socket, protocol, sys, data)

#with daemon.DaemonContext():
print('starting washer server...')
WasherServer = Washer_Server((common.WASHER_BIND_HOST, common.WASHER_BIND_PORT), Request_Handler)
WasherServer.serve_forever()
