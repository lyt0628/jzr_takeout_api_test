import pytest
import requests

from apis_order import api_add_order, api_find_orders_by_status
import util

@pytest.fixture
def setup_order():
    return {
        "consumerId": 1,
        "shopId": "1",
        "dishName": "JZR炸鸡"
    }


def test_add_order(setup_order):
    data = util.post(api_add_order(), setup_order)
    assert util.is_status_success(data)

def test_find_orders_by_Status():
    resp = requests.get(api_find_orders_by_status('WaitingDriverCaught'))
    body = util.extract_body(resp)
    data = body["data"]
    assert util.is_status_success(body)
    assert len(data) > 0