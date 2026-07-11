import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("REQRES_API_KEY")

#Assert list of users, Here we check the server returned a list the list is not empty

def test_user_list():
    response = requests.get(
        "https://reqres.in/api/users/2",
        headers={"x-api-key": API_KEY},
    )
    assert response.status_code == 200
    users = response.json()["data"]
    assert len(users)>0


def test_user_count():
    response = requests.get(
        "https://reqres.in/api/users/2",
        headers={"x-api-key": API_KEY},
    )
    users = response.json()["data"]
    assert len(users) ==5