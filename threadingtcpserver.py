
def factorial(nb):
    if nb== 0:
        return 1
    else:
        return factorial(nb-1) * nb
    
import socketserver

class MyHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            try:
#                 self.request.settimeout(3)
                messageB=self.request.recv(20)
                messageS=messageB.decode()
                print(f"message received: {messageS}")
                if messageS == "stop":
                    self.request.close()
                    break
                try:
                    resp=factorial(int(messageS))
                    self.request.send(f"factorial {messageS} is {resp}".encode())
                except:
                    self.request.send(f"Error processing {messageS} !!".encode())
            except:
                self.request.close()
                break

try:
    sock_srv=socketserver.ThreadingTCPServer(("sicourspc220", 34566), MyHandler)
    sock_srv.serve_forever()
except Exception as ex:
    print(ex)

