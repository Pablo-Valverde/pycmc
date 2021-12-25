from requests import Session
from KeyInfo import KeyInfo

COINMARKETCAP_MAIN_SERVER = "https://pro-api.coinmarketcap.com/"
COINMARKETCAP_TEST_SERVER = "https://sandbox-api.coinmarketcap.com/"
TEST_KEY = "b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c" #---- Sandbox test key for coinmarketcap test API ----#

class __wrapper:

    def __init__(self, api_key, version) -> None:
        self.api_key = api_key
        self.version = version
        self.testing = True if api_key == TEST_KEY else False
        self.__main_url = COINMARKETCAP_MAIN_SERVER if not self.testing else COINMARKETCAP_TEST_SERVER
        self.__headers = {
            "X-CMC_PRO_API_KEY": self.api_key
        }
        self.__session = Session()
        self.__session.headers.update(self.__headers)

    def __get(self, url, **kwargs):
        url = "{}{}{}".format(self.__main_url, self.version, url)
        response = self.__session.get(url, params=kwargs)
        return response

    def getKeyInfo(self):
        response = self.__get("/key/info")
        return KeyInfo(response)

    def getCryptoMap():
        pass

def start(api_key:str = TEST_KEY, version = "v1"):
    api_key = str(api_key)
    return __wrapper(api_key, version)
