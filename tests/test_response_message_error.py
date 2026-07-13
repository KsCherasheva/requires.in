import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("REQRES_API_KEY")


def test_response_message():
    response = requests.get(
        "https://reqres.in/api/users/23",
        headers={"x-api-key": API_KEY},
    )
    assert response.status_code == 404
    body = response.json()
    assert isinstance(body, dict)