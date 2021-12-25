from key import KeyInfo
from cryptocurrency import cryptocurrencyInfo, cryptocurrencyMapData
from requests import Session


COINMARKETCAP_MAIN_SERVER = "https://pro-api.coinmarketcap.com/"
COINMARKETCAP_TEST_SERVER = "https://sandbox-api.coinmarketcap.com/"
TEST_KEY = "b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c" #---- Sandbox key for coinmarketcap test API ----#

SORT_BY_ID = "id"
SORT_BY_CMC_RANK = "cmc_rank"

SORT_DIR_ASC = "asc"
SORT_DIR_DESC = "desc"

CRYPTOCURRENCY_TYPE_ALL = "all"
CRYPTOCURRENCY_TYPE_COINS = "coins"
CRYPTOCURRENCY_TYPE_TOKENS = "tokens"

TAG_ALL = "all"
TAG_DEFI = "defi"
TAG_FILESHARING = "filesharing"

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
        return KeyInfo.KeyInfo(response)

    def getCryptoMap(
                        self, listing_status = LISTING_STATUS_ACTIVE, start = 1, limit = None, 
                        sort = SORT_BY_ID, symbol = None, aux = "platform,first_historical_data,last_historical_data,is_active"
                    ):

        response = self.__get("/cryptocurrency/map", listing_status = listing_status, start = start, limit = limit, sort = sort, symbol = symbol, aux = aux)
        return cryptocurrencyMapData.crypMap(response)

    def getCryptInfo(
                        self, 
                        id = None, 
                        slug = None, 
                        symbol = None, 
                        address = None, 
                        aux = "urls,logo,description,tags,platform,date_added,notice"
                    ):
    
        if not (id or slug or symbol or address):
            raise RuntimeError("Must contain at least one of [id, symbol, slug, address]")
        response = self.__get("/cryptocurrency/info", id = id, slug = slug, symbol = symbol, address = address, aux = aux)
        return cryptocurrencyInfo.crypInfo(response)

    def getCryptLatestListing(
                                self, 
                                start = 1, 
                                limit = 100, 
                                price_min = None, 
                                price_max = None, 
                                market_cap_min = None, 
                                market_cap_max = None, 
                                volume_24h_min = None, 
                                volume_24h_max = None, 
                                circulating_supply_min = None, 
                                circulating_supply_max = None, 
                                percent_change_24h_min = None, 
                                percent_change_24h_max = None, 
                                convert = None, 
                                convert_id = None, 
                                sort, 
                                sort_dir = SORT_DIR_ASC, 
                                cryptocurrency_type = CRYPTOCURRENCY_TYPE_ALL, 
                                tag = TAG_ALL, 
                                aux = "num_market_pairs,cmc_rank,date_added,tags,platform,max_supply,circulating_supply,total_supply"
                            ):

        raise NotImplementedError()

def start(api_key:str = TEST_KEY, version = "v1"):
    api_key = str(api_key)
    __wrapper.wrapper = __wrapper(api_key, version)
    return __wrapper.wrapper

def getWrapper():
    if __wrapper.wrapper:
        return __wrapper.wrapper
    raise NoWrapperYet()
