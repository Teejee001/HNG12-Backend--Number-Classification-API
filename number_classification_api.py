from fastapi import FastAPI, Query
import requests
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
from fastapi import FastAPI, Query
from flask import Flask
import requests
import os
from fastapi.middleware.cors import CORSMiddleware
from multiprocessing import Process

# FastAPI app setup
fastapi_app = FastAPI()

# Enable CORS for FastAPI
fastapi_app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n: int) -> bool:
    return n == sum(i for i in range(1, n) if n % i == 0)

def is_armstrong(n: int) -> bool:
    digits = [int(d) for d in str(n)]
    power = len(digits)
    return sum(d ** power for d in digits) == n

def get_fun_fact(n: int) -> str:
    try:
        response = requests.get(f"http://numbersapi.com/{n}/math", timeout=5)
        if response.status_code == 200:
            return response.text
        return "No fun fact available."
    except requests.RequestException:
        return "Could not retrieve fun fact."

@fastapi_app.get("/api/classify-number")
def classify_number(number: int = Query(..., description="The number to classify")):
    properties = []
    if is_armstrong(number):
        properties.append("armstrong")
    properties.append("odd" if number % 2 != 0 else "even")

    return {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": sum(map(int, str(number))),
        "fun_fact": get_fun_fact(number)
    }

# Flask app setup
flask_app = Flask(__name__)

@flask_app.route("/")
def home():
    return "Hello, Railway!"

def run_flask():
    # Use the PORT environment variable provided by Railway or default to 5000
    port = int(os.environ.get("PORT", 5000))
    flask_app.run(host="0.0.0.0", port=port)

def run_fastapi():
    import uvicorn
    uvicorn.run(fastapi_app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    # Run Flask and FastAPI apps in separate processes
    fastapi_process = Process(target=run_fastapi)
    flask_process = Process(target=run_flask)

    fastapi_process.start()
    flask_process.start()

    fastapi_process.join()
    flask_process.join()

