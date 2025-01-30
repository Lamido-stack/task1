 Flask API Project

 Project Description

This project is a simple Flask API that returns basic information, including the HNG registered email, current datetime in ISO 8601 format, and the GitHub URL of the project’s codebase.

 Setup Instructions

Follow the steps below to run the project locally:

```
1. Clone the repository

First, clone the repository to your local machine:

bash
git clone <https://github.com/Lamido-stack/task1>

2. Create a virtual environment (optional but recommended)

python -m venv venv
.\venv\Scripts\activate

3. Install dependencies

Install the necessary dependencies listed in requirements.txt:

pip install -r requirements.txt

4. Run the app locally

python app.py

default Link :  http://127.0.0.1:5000/.


 ****API Documentation****

Endpoint URL

    GET http://127.0.0.1:5000/

Request

    Method: GET
    URL: http://127.0.0.1:5000/


Response Format
The response will be returned in JSON format:

{
  "email": "email@example.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://https://github.com/Lamido-stack/task1"
}

Example Usage

To test the API locally, open your browser or use a tool like Postman or curl to make a GET request to:

http://127.0.0.1:5000/

Example curl request:

curl http://127.0.0.1:5000

Example response:

{
  "email": "email@example.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/Lamido-stack/task1"
}

For more information or to hire Python developers, check out this link:
https://hng.tech/hire/python-developers
