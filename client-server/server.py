import zmq
import math

# Servidor: recebe um número do cliente e responde com o fatorial.
# Executa em máquina separada do cliente.
#
# Uso: python3 server.py
# O cliente conecta passando o IP deste servidor como argumento.

context = zmq.Context()
socket  = context.socket(zmq.REP)
socket.bind("tcp://*:12345")

print("[Server] Aguardando requisições na porta 12345...")

while True:
    message = socket.recv_string()

    if message == "STOP":
        socket.send_string("Server encerrado.")
        print("[Server] Comando STOP recebido. Encerrando.")
        break

    try:
        n      = int(message)
        result = math.factorial(n)
        reply  = f"fatorial({n}) = {result}"
        print(f"[Server] Requisição: {n} → Resposta: {reply}")
    except ValueError:
        reply = f"Erro: '{message}' não é um número inteiro válido."
        print(f"[Server] Erro ao processar: {message}")

    socket.send_string(reply)
