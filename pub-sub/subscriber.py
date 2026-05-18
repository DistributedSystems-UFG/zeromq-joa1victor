import zmq
import sys

# Subscriber: conecta ao publisher e filtra mensagens por tópico.
# Múltiplos subscribers podem rodar em máquinas diferentes simultaneamente.
#
# Uso: python3 subscriber.py <ip_publisher> <topico>
# Exemplos:
#   python3 subscriber.py 172.31.62.117 TEMP
#   python3 subscriber.py 172.31.62.117 HUM

if len(sys.argv) < 3:
    print("Uso: python3 subscriber.py <ip_publisher> <topico>")
    print("Tópicos disponíveis: TEMP, HUM")
    sys.exit(1)

publisher_ip = sys.argv[1]
topic        = sys.argv[2].upper()

context = zmq.Context()
socket  = context.socket(zmq.SUB)
socket.connect(f"tcp://{publisher_ip}:12345")
socket.setsockopt_string(zmq.SUBSCRIBE, topic)

print(f"[Subscriber] Conectado a {publisher_ip}:12345 | Tópico: {topic}")
print("[Subscriber] Aguardando mensagens... Pressione Ctrl+C para encerrar.\n")

try:
    while True:
        msg = socket.recv_string()
        print(f"[Subscriber] Recebido: {msg}")

except KeyboardInterrupt:
    print("\n[Subscriber] Encerrado.")
