import socket

host = socket.gethostname()  # 获取主机地址
port = 12345  # 设置端口号
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建TCP/IP套接字
s.bind((host, port))  # 绑定ip地址和端口号到套接字
s.listen(1)  # 设置最多监听数（连接数）
sock, addr = s.accept()  # 被动接受TCP客户端连接
print('successfully connect')
info = sock.recv(1024).decode()    # 接受客户端数据
while info != 'see you':
    if info:
        print("The message received is:"+info)       # 打印接收到的数据
    sendData = input('please input:')
    sock.send(sendData.encode())        # 发送TCP数据
    if sendData == 'see you':
        break
    info = sock.recv(1024).decode()     # 接受客户端数据
sock.close()                            # 关闭客户端套接字
s.close()                               # 关闭服务器套接字