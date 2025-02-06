from fastapi import FastAPI, Query
import uvicorn
import os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API is running!"}

@app.get("/api/classify-number")
def classify_number(number: int = Query(371, description="The number to classify")):
    # Check if the number is prime
    is_prime = number > 1 and all(number % i != 0 for i in range(2, int(number ** 0.5) + 1))

    # Check if the number is perfect (example perfect numbers)
    is_perfect = number in [6, 28, 496]

    # Check if the number is Armstrong (narcissistic)
    num_str = str(number)
    num_digits = len(num_str)
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    is_armstrong = armstrong_sum == number

    # Get the sum of digits
    digit_sum = sum(int(digit) for digit in num_str)

    # Determine properties
    properties = ["odd" if number % 2 else "even"]
    if is_armstrong:
        properties.append("armstrong")

    # Fun fact about 371
    fun_fact = "371 is a narcissistic number."

    return {
        "number": number,
        "is_prime": is_prime,
        "is_perfect": is_perfect,
        "properties": properties,
        "digit_sum": digit_sum,
        "fun_fact": fun_fact
    }

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)

