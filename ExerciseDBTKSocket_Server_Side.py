import socket

def getProduct(name):
    import sqlite3
    try:
        conn=sqlite3.connect(r"epfl.db")
        cursor=conn.cursor()
        cursor.execute (f"SELECT * FROM product where name='{name}'")
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return row
    except Exception as ex:
        print(ex)


try:
    sock_srv=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock_srv.bind(("localhost", 34566)) # nmap or netstat
    sock_srv.listen(2)
    while True:
        print("Server ready")
        sock_cli, addr_cli=sock_srv.accept()
        print(f"connection established with {addr_cli}")
        try:
                
            messageB=sock_cli.recv(20)
            # messageB is "bytes" object
            messageS=messageB.decode() # to transform bytes into str
            print(f"message received: {messageS}")
            
            resp=getProduct(messageS)
            if resp== None:
                resp=[]
            
            import pickle           
            sock_cli.send(pickle.dumps(resp))

        except:
            sock_cli.close()
            break
        
    sock_srv.close()
except Exception as ex:
    print(ex)

