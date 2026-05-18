import zmq

# Consumer: recebe e exibe os resultados finais processados pelo Worker.
# Etapa 3 do pipeline: Producer → Worker → Consumer
#
# Uso: python3 consumer.py
# O Worker deve conectar ao IP desta máquina.

context  = zmq.Context()
receiver = context.socket(zmq.PULL)
receiver.bind("tcp://*:5679")

print("[Consumer] Aguardando resultados na porta 5679...")
print("[Consumer] Pressione Ctrl+C para encerrar.\n")

total    = 0
count    = 0

try:
    while True:
        msg    = receiver.recv_string()
        number, result = msg.split(":")
        total  += int(result)
        count  += 1
        print(f"[Consumer] Recebeu: {number}² = {result} | Total acumulado: {total} | Itens: {count}")

except KeyboardInterrupt:
    print(f"\n[Consumer] Encerrado. Total de itens processados: {count} | Soma total: {total}")
