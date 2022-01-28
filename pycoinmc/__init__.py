import json
from . import exchange
from . import key as k
from . import cryptocurrency as crypt
from requests import Session
from .response import response


COINMARKETCAP_MAIN_SERVER =                                                     "https://pro-api.coinmarketcap.com/"
COINMARKETCAP_TEST_SERVER =                                                     "https://sandbox-api.coinmarketcap.com/"
TEST_KEY =                                                                      "b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c" #---- Sandbox key for coinmarketcap test API ----#

REQUEST_SUCCESS =                                                                200
BAD_REQUEST =                                                                    400
UNAUTHORIZED =                                                                   401
FORBIDDEN =                                                                      403
NOT_FOUND =                                                                      404
TOO_MANY_REQUESTS =                                                              429
INTERNAL_SERVER_ERROR =                                                          500

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
        self.__exchange = exchange.exchangeAPI(self.__get)

    def __get(self, url, **kwargs) -> response:
        url = "{}{}{}".format(self.__main_url, self.version, url)
        response = self.__session.get(url, params=kwargs)
        jsonified = json.loads(response.text)

        if not response.status_code == REQUEST_SUCCESS:
            try:
                status = jsonified["status"]
                error_message = status["error_message"]
                error_code = status["error_code"]
                raise RuntimeError("Error code: {}\n{}".format(error_code, error_message))
            except KeyError:
                pass
            raise RuntimeError("Can't connect to '{}'.".format(url))

        return jsonified

    def cryptocurrency(self) -> crypt.cryptAPI:
        return self.__cryptocurrency

    def key(self) -> k.keyAPI:
        return self.__key

    def exchange(self) -> exchange.exchangeAPI:
        return self.__exchange

def start(api_key:str = TEST_KEY, version = "v1") -> __wrapper:
    api_key = str(api_key)
    __wrapper.wrapper = __wrapper(api_key, version)
    return __wrapper.wrapper

def getWrapper() -> __wrapper:
    if __wrapper.wrapper:
        return __wrapper.wrapper
    raise NoWrapperYet()
