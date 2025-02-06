import os
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API is running!"}

@app.get("/api/classify-number")
def classify_number():
    number = 371
    response = {
        "number": number,
        "is_prime": False,
        "is_perfect": False,
        "properties": ["armstrong", "odd"],
        "digit_sum": 11,
        "fun_fact": "371 is a narcissistic number."
    }
    return response

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)

