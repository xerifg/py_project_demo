import socket

host = socket.gethostname()  # 获取主机地址
port = 12345  # 设置端口号
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
data = input('please input:')
s.sendto(data.encode(),(host,port))
print(s.recv(1024).decode())           # 打印接收到的数据
s.close()