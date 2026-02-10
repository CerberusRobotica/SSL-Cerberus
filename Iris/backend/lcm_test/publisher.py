import lcm
import time

lc = lcm.LCM()
channel = "IRIS_TEST"

print("📡 LCM Publisher de teste iniciado")

i = 0
while True:
    msg = f"Mensagem {i}".encode("utf-8")
    lc.publish(channel, msg)
    print(f"Enviado -> {channel}: {msg}")
    i += 1
    time.sleep(1)
