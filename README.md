# ZeroMQ-Examples — Execução Distribuída com Novas Funcionalidades

Modificação dos exemplos base da tarefa para execução em máquinas distintas
com adição de novas funcionalidades de aplicação em cada padrão de comunicação.

---

## Infraestrutura (AWS EC2)

7 instâncias EC2 na AWS conectadas via EFS compartilhado:

| Instância | IP Privado | Papel |
|-----------|------------|-------|
| SERVER | 172.31.62.117 | Servidor / Publisher / Producer |
| PEER1 | — | Cliente |
| PEER2 | — | Subscriber TEMP |
| PEER3 | — | Subscriber HUM |
| PEER4 | 172.31.56.99 | Consumer (pipeline) |
| PEER5 | — | Worker (pipeline) |
| PEER6 | — | Worker adicional (pipeline) |

---

## 1. Client-Server — Cálculo de Fatorial

**Nova funcionalidade:** o cliente envia números inteiros e o servidor
calcula e devolve o fatorial de cada um, em vez de apenas ecoar a mensagem.

```
Cliente (REQ) → envia número → Servidor (REP) → responde com fatorial
```

### Execução

**SERVER:**
```bash
cd client-server
python3 server.py
```

**PEER1:**
```bash
cd client-server
python3 client.py 172.31.62.117
```

---

## 2. Publish-Subscribe — Sensores por Tópico

**Nova funcionalidade:** o publisher publica em dois tópicos distintos
(`TEMP` para temperatura e `HUM` para humidade). Cada subscriber escolhe
qual tópico assinar, recebendo apenas as mensagens relevantes.

```
Publisher (PUB) → TEMP / HUM → Subscriber TEMP
                             → Subscriber HUM
```

### Execução

**SERVER:**
```bash
cd pub-sub
python3 publisher.py
```

**PEER2 (assina temperatura):**
```bash
cd pub-sub
python3 subscriber.py 172.31.62.117 TEMP
```

**PEER3 (assina humidade):**
```bash
cd pub-sub
python3 subscriber.py 172.31.62.117 HUM
```

---

## 3. Pipeline — Producer → Worker → Consumer (3 processos)

**Nova funcionalidade:** pipeline em cadeia com 3 processos distintos.
O Producer gera números aleatórios, o Worker (Consumer/Producer) calcula
o quadrado de cada número e encaminha ao Consumer final, que acumula
e exibe os resultados.

```
Producer (PUSH) → Worker (PULL/PUSH) → Consumer (PULL)
  gera números    calcula quadrado      acumula resultados
```

### Execução (ordem importante — Consumer e Worker primeiro)

**PEER4 — Consumer (primeiro):**
```bash
cd pipeline_producer-consumer
python3 consumer.py
```

**PEER5 — Worker (segundo):**
```bash
cd pipeline_producer-consumer
python3 worker.py 172.31.62.117 172.31.56.99
```

**SERVER — Producer (terceiro):**
```bash
cd pipeline_producer-consumer
python3 producer.py
```

---

## Modificações Realizadas

| Exemplo | Modificação |
|---------|-------------|
| Client-Server | Separado em `server.py` e `client.py`. Servidor calcula fatorial dos números recebidos. |
| Pub-Sub | Separado em `publisher.py` e `subscriber.py`. Publisher emite dois tópicos (`TEMP`, `HUM`). Subscriber filtra por tópico via argumento. |
| Pipeline | Transformado em cadeia de 3 processos: `producer.py` → `worker.py` → `consumer.py`. Worker processa (calcula quadrado) e encaminha ao consumer final. |
