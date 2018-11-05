import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 8888))
s.listen(3)

def getweb():
    try:
        sc, addr = s.accept()
        line = 'HTTP/1.1 200 OK\r\n'
        body = 'Content-Type: text/plain; charset=UTF-8\r\n<body>centos<\\body>\r\n'
        data = sc.recv(4096)
        print(str(data, encoding='utf-8'))
        sc.send(bytes(line+body, encoding='utf-8'))
        sc.close()
    finally:
        s.close()

getweb()
