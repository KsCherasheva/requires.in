import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("REQRES_API_KEY")
BASE_URL = "https://reqres.in/api/users"


def test_non_exist_user():
    response = requests.get(f"{BASE_URL}/999999", headers={"x-api-key": API_KEY})
    assert response.status_code == 404