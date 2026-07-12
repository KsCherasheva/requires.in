import os
import requests
import pytest
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("REQRES_API_KEY")

@pytest.fixture
def user_response():
    response = requests.get(
        "https://reqres.in/api/users/2",
        headers={"x-api-key": API_KEY},
    )
    return response