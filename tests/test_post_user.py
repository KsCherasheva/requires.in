import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("REQRES_API_KEY")


def test_create_user():
    body = {
        "name": "Mary",
        "job": "QA engineer"
    }

    response = requests.post(
        "https://reqres.in/api/users",
        headers={"x-api-key": API_KEY},
        json=body,
    )

    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Mary"
    assert data["job"] == "QA engineer"