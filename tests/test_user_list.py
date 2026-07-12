#Assert list of users, Here we check the server returned a list the list is not empty

def test_user_list(user_response):
    assert user_response.status_code == 200
    users =  user_response.json()["data"]
    assert len(users)>0


def test_user_count(user_response):
    users=user_response.json()["data"]
    assert len(users) ==5
