import key as k
import cryptocurrency as crypt
from requests import Session
from response import response

COINMARKETCAP_MAIN_SERVER =                                                     "https://pro-api.coinmarketcap.com/"
COINMARKETCAP_TEST_SERVER =                                                     "https://sandbox-api.coinmarketcap.com/"
TEST_KEY =                                                                      "b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c" #---- Sandbox key for coinmarketcap test API ----#

class NoWrapperYet(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class __wrapper:

    wrapper = None

    def __init__ (self, api_key, version) -> None:
        self.api_key = api_key
        self.version = version
        self.testing = True if api_key == TEST_KEY else False

        self.__main_url = COINMARKETCAP_MAIN_SERVER if not self.testing else COINMARKETCAP_TEST_SERVER
        self.__headers = {
            "X-CMC_PRO_API_KEY": self.api_key
        }
        self.__session = Session()
        self.__session.headers.update(self.__headers)

        self.__key = k.keyAPI(self.__get)
        self.__cryptocurrency = crypt.cryptAPI(self.__get)

    def __get(self, url, **kwargs) -> response:
        url = "{}{}{}".format(self.__main_url, self.version, url)
        response = self.__session.get(url, params=kwargs)
        return response

    def cryptocurrency(self) -> crypt.cryptAPI:
        return self.__cryptocurrency

    def key(self) -> k.keyAPI:
        return self.__key

def start(api_key:str = TEST_KEY, version = "v1") -> __wrapper:
    api_key = str(api_key)
    __wrapper.wrapper = __wrapper(api_key, version)
    return __wrapper.wrapper

def getWrapper() -> __wrapper:
    if __wrapper.wrapper:
        return __wrapper.wrapper
    raise NoWrapperYet()

cmc = start()
aux = cmc.cryptocurrency().info(id="1,2,3").data._1.urls.chat
pass