def factorial(nb):
    if nb== 0:
        return 1
    else:
        return factorial(nb-1) * nb

import socket

try:
    sock_srv=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock_srv.bind(("localhost", 34566)) # nmap or netstat
    sock_srv.listen(2)
    while True:
        print(f"Server ready")
        sock_cli, addr_cli=sock_srv.accept()
        print(f"connection established with {addr_cli}")
        while True:
            try:
                #sock_cli.settimeout(3)
                messageB=sock_cli.recv(20)
                # messageB is "bytes" object
                messageS=messageB.decode() # to transform bytes into str
                print(f"message received: {messageS}")
                if messageS == "stop":
                    sock_cli.close()
                    break
                try:
                    resp=factorial(int(messageS))
                    sock_cli.send(f"factorial {messageS} is {resp}".encode())
                except:
                    sock_cli.send(f"Error processing {messageS} !!".encode())
            except:
                sock_cli.close()
                break
        
    sock_srv.close()
except Exception as ex:
    print(ex)

