import zmq
import random
import time

# Producer: gera números aleatórios e os envia ao Worker para processamento.
# Etapa 1 do pipeline: Producer → Worker → Consumer
#
# Uso: python3 producer.py
# O Worker deve conectar ao IP desta máquina.

context = zmq.Context()
socket  = context.socket(zmq.PUSH)
socket.bind("tcp://*:5678")

print("[Producer] Enviando tarefas na porta 5678...")
print("[Producer] Aguarde o Worker conectar antes de iniciar.\n")
time.sleep(2)

for i in range(20):
    number = random.randint(1, 10)
    print(f"[Producer] Enviando número: {number}")
    socket.send_string(str(number))
    time.sleep(0.5)

print("[Producer] Todas as tarefas enviadas.")
