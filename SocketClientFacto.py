import socket
try:
    sock_cli=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock_cli.connect(("localhost", 34566))
    
    sock_cli.send(b"7")
    resp=sock_cli.recv(40)
    print(f"Response from server: {resp.decode()}")
   
    sock_cli.send("8".encode())
    resp=sock_cli.recv(40)
    
    print(f"Response from server: {resp.decode()}")
    sock_cli.send("stop".encode())
    sock_cli.close()
    
except Exception as ex:
    print(ex)

