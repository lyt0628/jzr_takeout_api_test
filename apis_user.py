from conf import api

def pat(s=''):
    if type(s) != 'str':
        s = str(s)
    if s != '' and not s.startswith('/'):
        s = '/' + s

    return api(f"/users{s}")

def api_add_consumer():
    return pat()

def api_find_consumer(id):
    return pat(id)

def api_consumer_logoff(id):
    return pat(f"/{id}/logoff")


