import key.KeyInfo
import cryptocurrency.cryptocurrencyMapData
from requests import Session


COINMARKETCAP_MAIN_SERVER = "https://pro-api.coinmarketcap.com/"
COINMARKETCAP_TEST_SERVER = "https://sandbox-api.coinmarketcap.com/"
TEST_KEY = "b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c" #---- Sandbox key for coinmarketcap test API ----#

SORT_BY_ID = "id"
SORT_BY_CMC_RANK = "cmc_rank"
AUX_DEFAULT = "platform,first_historical_data,last_historical_data,is_active"
LISTING_STATUS_ACTIVE = "active"
LISTING_STATUS_INACTIVE = "inactive"
LISTING_STATUS_UNTRACKED = "untracked"

class NoWrapperYet(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class __wrapper:

    wrapper = None

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
        return key.KeyInfo(response)

    def getCryptoMap(self, listing_status = LISTING_STATUS_ACTIVE, start = 1, limit = None, sort = SORT_BY_ID, symbol = None, aux = AUX_DEFAULT):
        response = self.__get("/cryptocurrency/map", listing_status = listing_status, start = start, limit = limit, sort = sort, symbol = symbol, aux = aux)
        return cryptocurrency.cryptocurrencyMapData.crypMap(response)

def start(api_key:str = TEST_KEY, version = "v1"):
    api_key = str(api_key)
    __wrapper.wrapper = __wrapper(api_key, version)
    return __wrapper.wrapper

def getWrapper():
    if __wrapper.wrapper:
        return __wrapper.wrapper
    raise NoWrapperYet()

crypto = start().getCryptoMap()
for coin in crypto.data:
    print("%s %s" % (coin.name, coin.id))