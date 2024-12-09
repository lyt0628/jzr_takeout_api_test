from conf import api

def pat(s=''):
    if type(s) != 'str':
        s = str(s)
    if s != '' and not s.startswith('/'):
        s = '/' + s

    return api(f"/shops{s}")


def api_add_shop():
    return pat()


def api_add_dish(shopId):
    return pat(f"/{shopId}/dishes")


def api_modify_dish_price(shopId, dishName):
    return pat(f"/{shopId}/dishes/{dishName}/modify_price")


def api_remove_dish(shopId, dishName):
    return pat(f"/{shopId}/dishes/{dishName}")

def api_get_all_valid_dishes():
    return pat("/dishes")