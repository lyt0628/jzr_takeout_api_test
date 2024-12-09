from conf_head import TEST_ENVIRONMENT


API_URL_PREFIX = ""
if TEST_ENVIRONMENT == "local":
    API_URL_PREFIX = "http://localhost:8888"
else:
    API_URL_PREFIX = "http://lyt0628.icu/api"



def api(path):
    return f"{API_URL_PREFIX}{path}"




