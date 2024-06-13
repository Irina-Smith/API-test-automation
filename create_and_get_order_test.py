import data
import sender_stand_request

def test_create_and_get_order():
    response = sender_stand_request.post_new_order(data.order_body)
    number_track = response.json()["track"]
    order_response = sender_stand_request.get_order(number_track)
    assert order_response.status_code == 200