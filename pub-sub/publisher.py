import zmq
import time
import random

context = zmq.Context()
socket  = context.socket(zmq.PUB)
socket.bind("tcp://*:12345")

print("[Publisher] Publicando nos tópicos TEMP e HUM (porta 12345)...")
print("[Publisher] Pressione Ctrl+C para encerrar.\n")

try:
    while True:
        temp = round(random.uniform(15.0, 40.0), 2)
        hum  = round(random.uniform(30.0, 90.0), 2)

        msg_temp = f"TEMP {temp}°C"
        msg_hum  = f"HUM {hum}%"

        socket.send_string(msg_temp)
        print(f"[Publisher] {msg_temp}")

        socket.send_string(msg_hum)
        print(f"[Publisher] {msg_hum}")

        time.sleep(3)

except KeyboardInterrupt:
    print("\n[Publisher] Encerrado.")
