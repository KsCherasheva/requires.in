import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("REQRES_API_KEY")

#Assert data int type Check that the field exists

def test_user_has_avatar():
    response = requests.get(
        "https://reqres.in/api/users/2",
        headers={"x-api-key": API_KEY},
    )

    data = response.json()

    assert "avatar" in data["data"]




def test_user_data():
    response = requests.get(
        "https://reqres.in/api/users/2",
        headers={"x-api-key": API_KEY},
    )

    user = response.json()["data"]

    assert isinstance(user["id"], int)