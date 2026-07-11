import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("REQRES_API_KEY")

def test_response_time():
    response = requests.get(
        "https://reqres.in/api/users/2",
        headers={"x-api-key": API_KEY},
    )

    assert response.elapsed.total_seconds()<2