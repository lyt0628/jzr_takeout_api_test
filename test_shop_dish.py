import pytest
import requests

from apis_shop import api_add_dish, api_modify_dish_price, api_remove_dish, api_get_all_valid_dishes
import util

@pytest.fixture
def setup_shop_zhaji():
    return {
        "shopId": 1,
        "dishName": "JZR炸鸡",
        "price": 300.666,

    }


# def test_add_dish(setup_shop_zhaji):
#     data = util.post(api_add_dish(shopId=1), setup_shop_zhaji)
#     assert util.is_status_success(data)


def test_modify_dish_price(setup_shop_zhaji):
    data = util.post(api_modify_dish_price(shopId=setup_shop_zhaji["shopId"],
                                           dishName=setup_shop_zhaji["dishName"]), 
                     695030452.666)
    assert util.is_status_success(data)


def test_remove_dish(setup_shop_zhaji):
    body = requests.delete(api_remove_dish(shopId=setup_shop_zhaji["shopId"],
                                     dishName=setup_shop_zhaji["dishName"]))
    data = util.extract_body(body)
    assert util.is_status_success(data)



def test_get_all_valid_dishes():
    body = requests.get(api_get_all_valid_dishes())
    data = util.extract_body(body)
    assert util.is_status_success(data)