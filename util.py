import json

def dumps(obj):
    return json.dumps(obj=obj)

def loads(json_str):
    return json.loads(json_str)

def extract_body(resp):
    return loads(resp.text)


def is_status_success(o : dict):
    return o["status"] == "success"


def is_status_failed(o : dict):
    return o["status"] == "failed"


headers = {'Content-Type': 'application/json'}


import pytest
import requests
import time

def post(url, obj=None):
    resp = requests.post(url=url, 
                         data=dumps(obj),
                         headers=headers)
    return extract_body(resp)

