import key
import cryptocurrency
from requests import Session


COINMARKETCAP_MAIN_SERVER = "https://pro-api.coinmarketcap.com/"
COINMARKETCAP_TEST_SERVER = "https://sandbox-api.coinmarketcap.com/"
TEST_KEY = "b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c" #---- Sandbox key for coinmarketcap test API ----#

MAP_SORT_BY_ID = "id"
MAP_SORT_BY_CMC_RANK = "cmc_rank"

LISTING_SORT_BY_MARKET_CAP = "market_cap"
LISTING_SORT_BY_MARKET_CAP_STRICT = "market_cap_strict"
LISTING_SORT_BY_NAME = "name"
LISTING_SORT_BY_SYMBOL = "symbol"
LISTING_SORT_BY_DATE_ADDED = "date_added"
LISTING_SORT_BY_PRICE = "price"
LISTING_SORT_BY_CIRCULATING_SUPPLY = "circulating_supply"
LISTING_SORT_BY_TOTAL_SUPPLY = "total_supply"
LISTING_SORT_BY_MAX_SUPPLY = "max_supply"
LISTING_SORT_BY_NUM_MARKET_PAIRS = "num_market_pairs"
LISTING_SORT_BY_MARKET_CAP_BY_TOTAL_SUPPLY_STRICT = "market_cap_by_total_supply_strict"
LISTING_SORT_BY_VOLUME_24H = "volume_24h"
LISTING_SORT_BY_VOLUME_7D = "volume_7d"
LISTING_SORT_BY_VOLUME_30D = "volume_30d"
LISTING_SORT_BY_PERCENT_CHANGE_1H = "percent_change_1h"
LISTING_SORT_BY_PERCENT_CHANGE_24H = "percent_change_24h"
LISTING_SORT_BY_PERCENT_CHANGE_7D = "percent_change_7d"

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
        response = self.__get(
                                url="/key/info"
                            )
        return key.Info(response)

    def getCryptoMap(
                        self, 
                        listing_status =                    LISTING_STATUS_ACTIVE, 
                        start =                             1, 
                        limit =                             None, 
                        sort =                              MAP_SORT_BY_ID, 
                        symbol =                            None, 
                        aux =                               "platform,first_historical_data,last_historical_data,is_active"
                    ):

        response = self.__get(
                                url="/cryptocurrency/map", 
                                listing_status=listing_status, 
                                start=start, 
                                limit=limit, 
                                sort=sort, 
                                symbol=symbol, 
                                aux=aux
                            )
        return cryptocurrency.Map(response)

    def getCryptInfo(
                        self, 
                        id =                                None, 
                        slug =                              None, 
                        symbol =                            None, 
                        address =                           None, 
                        aux =                               "urls,logo,description,tags,platform,date_added,notice"
                    ):

        response = self.__get(
                                url="/cryptocurrency/info", 
                                id=id, 
                                slug=slug, 
                                symbol=symbol, 
                                address=address, 
                                aux=aux
                            )

        return cryptocurrency.Info(response)

    def getCryptLatestListing(
                                self, 
                                start =                     1, 
                                limit =                     100, 
                                price_min =                 None, 
                                price_max =                 None, 
                                market_cap_min =            None, 
                                market_cap_max =            None, 
                                volume_24h_min =            None, 
                                volume_24h_max =            None, 
                                circulating_supply_min =    None, 
                                circulating_supply_max =    None, 
                                percent_change_24h_min =    None, 
                                percent_change_24h_max =    None, 
                                convert =                   None, 
                                convert_id =                None, 
                                sort =                      LISTING_SORT_BY_MARKET_CAP, 
                                sort_dir =                  SORT_DIR_ASC, 
                                cryptocurrency_type =       CRYPTOCURRENCY_TYPE_ALL, 
                                tag =                       TAG_ALL, 
                                aux =                       "num_market_pairs,cmc_rank,date_added,tags,platform,max_supply,circulating_supply,total_supply"
                            ):

        response = self.__get(
                                url="/cryptocurrency/info",
                                start=start,
                                limit=limit,
                                price_min=price_min,
                                price_max=price_max,
                                market_cap_min=market_cap_min,
                                market_cap_max=market_cap_max,
                                volume_24h_min=volume_24h_min,
                                volume_24h_max=volume_24h_max,
                                circulating_supply_min=circulating_supply_min,
                                circulating_supply_max=circulating_supply_max,
                                percent_change_24h_min=percent_change_24h_min,
                                percent_change_24h_max=percent_change_24h_max,
                                convert=convert,
                                convert_id=convert_id,
                                sort=sort,
                                sort_dir=sort_dir,
                                cryptocurrency_type=cryptocurrency_type,
                                tag=tag,
                                aux=aux
                            )

        return cryptocurrency.LatestListing(response)

def start(api_key:str = TEST_KEY, version = "v1"):
    api_key = str(api_key)
    __wrapper.wrapper = __wrapper(api_key, version)
    return __wrapper.wrapper

def getWrapper():
    if __wrapper.wrapper:
        return __wrapper.wrapper
    raise NoWrapperYet()

print(start().getCryptLatestListing())