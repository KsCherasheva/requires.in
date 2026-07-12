# Assert get user
def test_get_user(user_response):
    assert user_response.status_code == 200