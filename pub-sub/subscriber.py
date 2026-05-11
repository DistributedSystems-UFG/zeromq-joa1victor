import zmq, time
import sys

publisher_ip = sys.argv[1] if len(sys.argv) > 1 else "localhost"

context = zmq.Context()
socket = context.socket(zmq.SUB)                            # create a subscriber socket
socket.connect("tcp://" + publisher_ip + ":12345")          # connect to the publisher
socket.setsockopt(zmq.SUBSCRIBE, b"TIME")                   # subscribe to TIME messages

for i in range(5):       # Five iterations
  msg = socket.recv()    # receive a message related to subscription
  print(msg.decode())    # print the result
