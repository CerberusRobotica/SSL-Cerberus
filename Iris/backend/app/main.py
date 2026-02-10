from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from threading import Thread

from subscribers.test.subscriber import start as start_test
from subscribers.test.state import test_state 

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup():
    Thread(target=start_test, daemon=True).start()
    print("🚀 Subscriber TEST iniciado")

@app.get("/test")
def test_data():
    data = test_state.get()
    return {
        "message": data.decode() if data else None
    }
