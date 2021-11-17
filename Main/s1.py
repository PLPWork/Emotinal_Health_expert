import socket


def main():
    s = socket.socket()
    host = socket.gethostname()
    port = 6001
    s.connect((host, port))
    inpt = input('type anything and click enter... ')
    s.send(bytes(inpt, "UTF-8"))
    print("the message has been sent")
    print (s.recv(1024).decode("utf-8", "ignore") )
    
main()