import zmq
import sys


if len(sys.argv) < 3:
    print("Uso: python3 worker.py <ip_producer> <ip_consumer>")
    sys.exit(1)

producer_ip = sys.argv[1]
consumer_ip = sys.argv[2]

context  = zmq.Context()

receiver = context.socket(zmq.PULL)
receiver.connect(f"tcp://{producer_ip}:5678")

sender   = context.socket(zmq.PUSH)
sender.connect(f"tcp://{consumer_ip}:5679")

print(f"[Worker] Conectado ao Producer em {producer_ip}:5678")
print(f"[Worker] Encaminhando resultados ao Consumer em {consumer_ip}:5679")
print("[Worker] Aguardando tarefas... Pressione Ctrl+C para encerrar.\n")

try:
    while True:
        number = int(receiver.recv_string())
        result = number ** 2
        print(f"[Worker] Recebeu: {number} → Calculou: {number}² = {result} → Encaminhando...")
        sender.send_string(f"{number}:{result}")

except KeyboardInterrupt:
    print("\n[Worker] Encerrado.")
