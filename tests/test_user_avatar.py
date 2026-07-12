
#Assert data int type Check that the field exists

def test_user_has_avatar(user_response):
    data = user_response.json()
    assert "avatar" in data["data"]

def test_user_data(user_response):
    data_int = user_response.json()["data"]
    assert isinstance(data_int["id"], int)