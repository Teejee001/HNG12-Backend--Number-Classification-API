import os
import uvicorn
import math
import requests
from fastapi import FastAPI, Query, HTTPException

# Initialize FastAPI app
app = FastAPI()

# Root route
@app.get("/")
async def root():
    return {
        "message": "Welcome to the Number Classification API!",
        "usage": "Visit /api/classify-number?number=<your_number> to classify a number."
    }

# Helper function to check if a number is prime
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Helper function to check if a number is a perfect number
def is_perfect(n: int) -> bool:
    return n > 0 and sum(i for i in range(1, n) if n % i == 0) == n

# Helper function to check if a number is an Armstrong number
def is_armstrong(n: int) -> bool:
    digits = [int(d) for d in str(n)]
    return sum(d ** len(digits) for d in digits) == n

# Helper function to fetch a fun fact about a number from the Numbers API
def get_fun_fact(n: int) -> str:
    try:
        response = requests.get(f"http://numbersapi.com/{n}")
        if response.status_code == 200:
            fact = response.text
            # Check if the fact is a placeholder or generic message
            if "missing a fact" in fact.lower() or "boring number" in fact.lower():
                # Provide a custom fact for Armstrong numbers
                if is_armstrong(n):
                    digits = [int(d) for d in str(n)]
                    power = len(digits)
                    explanation = " + ".join(f"{d}^{power}" for d in digits)
                    return f"{n} is an Armstrong number because {explanation} = {n}."
                else:
                    return f"{n} is an interesting number."
            return fact
    except Exception:
        pass
    return f"{n} is an interesting number."

# API endpoint to classify a number
@app.get("/api/classify-number")
async def classify_number(
    number: str = Query(..., description="Number to classify")
):
    # Validate input
    if not number.lstrip('-').isdigit():
        raise HTTPException(
            status_code=400,
            detail={
                "number": number,
                "error": True
            }
        )

    num = int(number)
    properties = []

    # Check number properties
    if is_armstrong(num):
        properties.append("armstrong")
    if num % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")

    # Build response
    response = {
        "number": num,
        "is_prime": is_prime(num),
        "is_perfect": is_perfect(num),
        "properties": properties,
        "digit_sum": sum(int(d) for d in str(num)),
        "fun_fact": get_fun_fact(num)
    }

    return response

# Run the app with Uvicorn
if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))  # Use Railway's PORT or default to 8080
    uvicorn.run(app, host="0.0.0.0", port=port)
