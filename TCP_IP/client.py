import socket

s =socket.socket()
host = socket.gethostname()
port = 12345
s.connect((host,port))         # 主动初始化TCP服务器连接
print('successfully connect to server')
info = ''
while info!='see you':
    sendData = input('please input:')
    s.send(sendData.encode())      # 发送TCP数据
    if sendData == 'see you':
        break
    info = s.recv(1024).decode()    # 接受服务器发来的数据
    print('The message received is:'+info)
s.close()                           # 关闭套接字
