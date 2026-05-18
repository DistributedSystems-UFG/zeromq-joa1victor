import zmq
import sys

# Cliente: envia números ao servidor e exibe o fatorial calculado.
# Executa em máquina separada do servidor.
#
# Uso: python3 client.py <ip_servidor>
# Exemplo: python3 client.py 172.31.62.117

if len(sys.argv) < 2:
    print("Uso: python3 client.py <ip_servidor>")
    sys.exit(1)

server_ip = sys.argv[1]

context = zmq.Context()
socket  = context.socket(zmq.REQ)
socket.connect(f"tcp://{server_ip}:12345")

print(f"[Client] Conectado ao servidor em {server_ip}:12345")

numbers = [1, 5, 10, 15, 20]

for n in numbers:
    socket.send_string(str(n))
    reply = socket.recv_string()
    print(f"[Client] Enviou: {n} → Recebeu: {reply}")

socket.send_string("STOP")
print(socket.recv_string())
