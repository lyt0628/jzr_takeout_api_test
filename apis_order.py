from typing import Literal

from conf import api

def pat(s=''):
    if type(s) != 'str':
        s = str(s)

    return api(f"/orders{s}")


def api_add_order():
    return pat()


def api_find_orders_by_status(
        status : Literal['WaitingConsumerPay', 'ConsumerCanceled', 'ConsumerPaid', 'ShopCaught', 
                         'WaitingDriverCaught', 'DriverCaught', 'DriverConfirmed', 'ConsumerConfirmed']):
    return pat(f"?status={status}")