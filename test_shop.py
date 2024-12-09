
import pytest
import requests

from apis_shop import api_add_shop
import util

@pytest.fixture
def setup_shop_zhajidian():
    return {
        "sellerId": 1,
        "shopName": "JZR炸鸡店",
    }

def test_add_shop(setup_shop_zhajidian):
    data = util.post(api_add_shop(), setup_shop_zhajidian)
    assert util.is_status_success(data)



