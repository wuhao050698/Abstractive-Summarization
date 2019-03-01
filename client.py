# -*- coding: utf-8 -*-
# @Time    : 2019/2/26 15:58
# @Author  : wu
# @FileName: client.py
# @Project: Global-Encoding-master


import socket
while(True):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("localhost", 8081))  # 连接服务器
    temp = input()
    temp=bytes(temp, encoding = "utf8")
    sock.sendall(temp)  # 将消息输出到发送缓冲 send buffer
    print(str(sock.recv(10240), encoding = "utf-8"))
#print(sock.recv(1024)) # 从接收缓冲 recv buffer 中读响应
    sock.close() # 关闭套接字...
