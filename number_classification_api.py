from fastapi import FastAPI, Query
import requests
import os
import uvicorn

app = FastAPI()

# Enable CORS
from fastapi.middleware.cors import CORSMiddleware
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

@app.get("/api/classify-number")
def classify_number(number: int = Query(..., description="The number to classify")):
    if not isinstance(number, int):
        return {"number": str(number), "error": True}

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

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # Use port 8080 from Railway
    uvicorn.run(app, host="0.0.0.0", port=port)

