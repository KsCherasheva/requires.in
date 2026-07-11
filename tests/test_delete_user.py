import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("REQRES_API_KEY")

def test_delete_user():
    response = requests.delete(
        "https://reqres.in/api/users/2",
        headers={"x-api-key": API_KEY},
    )


    assert response.status_code == 204