#verify response


def test_get_user(user_response):
    assert user_response.status_code == 200


#Verify response time

def test_response_time(user_response):

    assert user_response.elapsed.total_seconds()<2

#Verify  structure

def test_user_list_matches_schema(user_response):
    body = user_response.json()
    assert set(body.keys()) >= { "_meta",  "data", "support"}