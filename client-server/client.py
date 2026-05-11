import zmq
import sys

server_ip = sys.argv[1] if len(sys.argv) > 1 else "localhost"

context = zmq.Context()
socket  = context.socket(zmq.REQ)                       
socket.connect("tcp://" + server_ip + ":12345")         

socket.send(b"Hello world")            
message = socket.recv()                 
socket.send(b"STOP")                    
socket.recv()                          
print(message.decode())                
