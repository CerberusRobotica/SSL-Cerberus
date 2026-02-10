import lcm
from subscribers.test.state import test_state

CHANNEL = "IRIS_TEST"

def handler(channel, data):
    print(f"[TEST] Recebido: {data}")
    test_state.update(data)

def start():
    lc = lcm.LCM()
    lc.subscribe(CHANNEL, handler)

    print("🟢 Subscriber TEST ativo")

    while True:
        lc.handle()
