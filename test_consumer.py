
import pytest
import requests


from conf import api


def test_logoff():
    response = requests.post(url=api("/consumers/1/logoff"))
    print(response.status_code)  # 打印响应状态码
    print(response.text) 