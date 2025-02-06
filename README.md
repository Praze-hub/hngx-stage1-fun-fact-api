# Numbers API with Django REST Framework

This project is a simple API built using Django REST Framework that fetches interesting mathematical properties and fun facts about a given number using the [Numbers API](http://numbersapi.com/).

## Features
- Fetches a fun fact about a number from the Numbers API.
- Computes and returns mathematical properties such as:
  - Whether the number is prime.
  - Whether the number is a perfect number.
  - Classification as even, odd, or Armstrong number.
  - The sum of its digits.

## Installation
### Prerequisites
Ensure you have Python installed. You can download it from [python.org](https://www.python.org/).

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/numbers-api-django.git
   cd numbers-api-django
   ```
2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```sh
   python manage.py migrate
   ```
5. Start the development server:
   ```sh
   python manage.py runserver
   ```

## Usage
### API Endpoint
Send a GET request to the following endpoint:
```sh
http://127.0.0.1:8000/api/number/<number>/
```
#### Example Response
```json
{
  "number": 371,
  "is_prime": false,
  "is_perfect": false,
  "properties": ["armstrong", "odd"],
  "digit_sum": 11,
  "fun fact": "371 is an armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```


