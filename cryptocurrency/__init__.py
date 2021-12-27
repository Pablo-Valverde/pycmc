import _cmcBranch
from cryptocurrency.Info import Info
from cryptocurrency.Map import Map
from response import response as cmcresponse

MAP_SORT_BY_ID =                                                                "id"
MAP_SORT_BY_CMC_RANK =                                                          "cmc_rank"

LISTING_SORT_BY_MARKET_CAP =                                                    "market_cap"
LISTING_SORT_BY_MARKET_CAP_STRICT =                                             "market_cap_strict"
LISTING_SORT_BY_NAME =                                                          "name"
LISTING_SORT_BY_SYMBOL =                                                        "symbol"
LISTING_SORT_BY_DATE_ADDED =                                                    "date_added"
LISTING_SORT_BY_PRICE =                                                         "price"
LISTING_SORT_BY_CIRCULATING_SUPPLY =                                            "circulating_supply"
LISTING_SORT_BY_TOTAL_SUPPLY =                                                  "total_supply"
LISTING_SORT_BY_MAX_SUPPLY =                                                    "max_supply"
LISTING_SORT_BY_NUM_MARKET_PAIRS =                                              "num_market_pairs"
LISTING_SORT_BY_MARKET_CAP_BY_TOTAL_SUPPLY_STRICT =                             "market_cap_by_total_supply_strict"
LISTING_SORT_BY_VOLUME_24H =                                                    "volume_24h"
LISTING_SORT_BY_VOLUME_7D =                                                     "volume_7d"
LISTING_SORT_BY_VOLUME_30D =                                                    "volume_30d"
LISTING_SORT_BY_PERCENT_CHANGE_1H =                                             "percent_change_1h"
LISTING_SORT_BY_PERCENT_CHANGE_24H =                                            "percent_change_24h"
LISTING_SORT_BY_PERCENT_CHANGE_7D =                                             "percent_change_7d"

SORT_DIR_ASC =                                                                  "asc"
SORT_DIR_DESC =                                                                 "desc"

CRYPTOCURRENCY_TYPE_ALL =                                                       "all"
CRYPTOCURRENCY_TYPE_COINS =                                                     "coins"
CRYPTOCURRENCY_TYPE_TOKENS =                                                    "tokens"

TAG_ALL =                                                                       "all"
TAG_DEFI =                                                                      "defi"
TAG_FILESHARING =                                                               "filesharing"

LISTING_STATUS_ACTIVE =                                                         "active"
LISTING_STATUS_INACTIVE =                                                       "inactive"
LISTING_STATUS_UNTRACKED =                                                      "untracked"

class cryptAPI(_cmcBranch.cmcBranch):
    
    def __init__(self, __get) -> None:
        super().__init__(__get)

    def map (
        self, 
        listing_status =                    LISTING_STATUS_ACTIVE,
        start =                             1,
        limit =                             None,
        sort =                              MAP_SORT_BY_ID,
        symbol =                            None,
        aux =                               "platform,first_historical_data,last_historical_data,is_active"
    ):

        assert start >= 1

        response = self._get (
            url = "/cryptocurrency/map",
            listing_status = listing_status,
            start = start,
            limit = limit,
            sort = sort,
            symbol = symbol,
            aux = aux
        )
        return Map(response)

    def info (
        self,
        id =                                None,
        slug =                              None,
        symbol =                            None,
        address =                           None,
        aux =                               "urls,logo,description,tags,platform,date_added,notice"
    ):

        assert id or slug or symbol or address, "Atleast [id, slug, symbol or address] must be present"
        response = self._get (
            url = "/cryptocurrency/info",
            id = id,
            slug = slug,
            symbol = symbol,
            address = address,
            aux = aux
        )
        return Info(response)

    def latest_quotes(
        self,
        id =                                None,
        slug =                              None,
        symbol =                            None,
        convert =                           None,
        convert_id =                        None,
        aux =                               "num_market_pairs,cmc_rank,date_added,tags,platform,max_supply,circulating_supply,total_supply,is_active,is_fiat",
        skip_invalid =                      False
    ):

        assert id or slug or symbol, "Atleast [id, slug or symbol] must be present"
        response = self._get (
            url = "/cryptocurrency/quotes/latest",
            id = id,
            slug = slug,
            symbol = symbol,
            convert = convert,
            convert_id = convert_id,
            aux = aux,
            skip_invalid = skip_invalid
        )
        return cmcresponse(response)

    def categories (
        self,
        start =                             1,
        limit =                             None,
        id =                                None,
        slug =                              None,
        symbol =                            None
    ):
        
        response = self._get (
            url = "/cryptocurrency/categories",
            start = start,
            limit = limit,
            id = id,
            slug = slug,
            symbol = symbol
        )
        return cmcresponse(response)

    def category (
        self,
        id,
        start =                             1,
        limit =                             100,
        convert =                           None,
        convert_id =                        None
    ):

        response = self._get (
            url = "/cryptocurrency/categories",
            id = id,
            start = start,
            limit = limit,
            convert = convert,
            convert_id = convert_id
        )
        return cmcresponse(response)