# HNG12-Backend--Number-Classification-API
# Number Classification API

## Overview
The **Number Classification API** is a web service that accepts a number as input and returns interesting mathematical properties about it, along with a fun fact.

## Features
- Determines if a number is **prime** or **perfect**.
- Identifies properties such as **odd**, **even**, or **Armstrong number**.
- Calculates the **sum of digits**.
- Fetches a **fun fact** about the number using the [Numbers API](http://numbersapi.com/).

## Technologies Used
- **Programming Language:** Python
- **Framework:** FastAPI / Flask (depending on your implementation)
- **Deployment:** Hosted on a publicly accessible endpoint
- **Version Control:** Git & GitHub
- **Data Handling:** Numbers API
- **Security:** CORS enabled

## API Endpoints
### 1. Classify a Number
**Endpoint:**
```http
GET /api/classify-number?number={number}
```
**Request Parameters:**
- `number` (integer) - The number to classify

**Success Response (200 OK):**
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

**Error Response (400 Bad Request):**
```json
{
    "number": "alphabet",
    "error": true
}
```

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- Git
- Virtual Environment (optional but recommended)

### Steps to Run Locally
1. **Clone the Repository**
```bash
git clone https://github.com/Teejee001/HNG12-Backend--Number-Classification-API.git
cd HNG12-Backend--Number-Classification-API
```
2. **Set up a Virtual Environment** (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
```
3. **Install Dependencies**
```bash
pip install -r requirements.txt
```
4. **Run the API**
```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --reload  # For FastAPI
# OR
python app.py  # If using Flask
```

## Deployment
- The API is deployed to **[Your Public Endpoint](#)**
- Uses **CORS handling** for cross-origin requests

## Testing the API
You can test the API using:
- **Postman**
- **cURL**
- **Your Web Browser**
```bash
curl -X GET "https://your-deployed-api.com/api/classify-number?number=371"
```

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository
2. Create a new branch (`feature-xyz`)
3. Commit your changes
4. Push to your fork
5. Create a pull request

## License
This project is licensed under the **MIT License**.

## Contact
- **GitHub Repo:** https://github.com/Teejee001/HNG12-Backend--Number-Classification-API
- **Email:** Olatunjibalogun025@gmail.com
