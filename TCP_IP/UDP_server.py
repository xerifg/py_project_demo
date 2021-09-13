import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # 创建UDP套接字
host = socket.gethostname()  # 获取主机地址
port = 12345  # 设置端口号
s.bind((host, port))  # 绑定ip地址和端口号到套接字
print('successfully bind')
data, addr = s.recvfrom(1024)
print('The message received is:' + data.decode())
print('Received from %s:%s.' % addr)
sendData = input('please input:')
s.sendto(sendData.encode(),addr)
s.close()