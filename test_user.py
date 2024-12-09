import pytest
import requests

from apis_user import api_add_consumer, api_find_consumer, api_consumer_logoff
import util

@pytest.fixture
def setup_consumer_lisi():
    return {
        # "id": id,
        "userName": "lisi",
        "pwd": 123456,
        "phone": 12345678910,
        "status": 0
    }

def test_add_consumer(setup_consumer_lisi):
    data = util.post(api_add_consumer(), setup_consumer_lisi)
    assert util.is_status_success(data)

def test_logoff():
    data = util.post(api_consumer_logoff(1))
    assert util.is_status_success(data)

def test_find_consumer():
    resp = requests.get(url=api_find_consumer(2))
    body = util.extract_body(resp)
    data = body['data']
    assert util.is_status_success(body)
    assert 'lisi' == data["username"]