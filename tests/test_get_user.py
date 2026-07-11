import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("REQRES_API_KEY")

# Assert get user
def test_get_user():
    url = "https://reqres.in/api/users?page=2"
    headers = {"x-api-key": API_KEY}

    print("КЛЮЧ КОТОРЫЙ РЕАЛЬНО ОТПРАВЛЯЕТСЯ:", repr(API_KEY))

    response = requests.get(url, headers=headers)

    assert response.status_code == 200