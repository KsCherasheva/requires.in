
def test_response_time(user_response):

    assert user_response.elapsed.total_seconds()<2