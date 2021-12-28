import _cmcBranch
from cryptocurrency.Categories import Categories
from cryptocurrency.Info import Info
from cryptocurrency.LatestListing import LatestListing
from cryptocurrency.Map import Map
from cryptocurrency.LatestQuotes import LatestQuotes
from cryptocurrency.Category import Category
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
    ) -> Map:

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
        return Map(response)._iterate()

    def info (
        self,
        id =                                None,
        slug =                              None,
        symbol =                            None,
        address =                           None,
        aux =                               "urls,logo,description,tags,platform,date_added,notice"
    ) -> Info:

        assert id or slug or symbol or address, "Atleast [id, slug, symbol or address] must be present"
        response = self._get (
            url = "/cryptocurrency/info",
            id = id,
            slug = slug,
            symbol = symbol,
            address = address,
            aux = aux
        )
        return Info(response)._iterate()

    def listings_latest(
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
        sort = LISTING_SORT_BY_MARKET_CAP,
        sort_dir = SORT_DIR_ASC,
        cryptocurrency_type = CRYPTOCURRENCY_TYPE_ALL,
        tag = TAG_ALL,
        aux = "num_market_pairs,cmc_rank,date_added,tags,platform,max_supply,circulating_supply,total_supply" 
    ) -> LatestListing:
        
        assert start >= 1
        assert limit >= 1 and limit <= 5000
        if price_min: assert price_min >= 0
        if price_max: assert price_max >= 0
        if market_cap_min: assert market_cap_min >= 0
        if market_cap_max: assert market_cap_max >= 0
        if volume_24h_min: assert volume_24h_min >= 0
        if volume_24h_max: assert volume_24h_max >= 0
        if circulating_supply_min: assert circulating_supply_min >= 0
        if circulating_supply_max: assert circulating_supply_max >= 0
        if percent_change_24h_min: assert percent_change_24h_min >= -100
        if percent_change_24h_max: assert percent_change_24h_max >= -100
        response = self._get (
            url = "/cryptocurrency/listings/latest",
            start = start,
            limit = limit,
            price_min = price_min,
            price_max = price_max,
            market_cap_min = market_cap_min,
            market_cap_max = market_cap_max,
            volume_24h_min = volume_24h_min,
            volume_24h_max = volume_24h_max,
            circulating_supply_min = circulating_supply_min,
            circulating_supply_max = circulating_supply_max,
            percent_change_24h_min = percent_change_24h_min,
            percent_change_24h_max = percent_change_24h_max,
            convert = convert,
            convert_id = convert_id,
            sort = sort,
            sort_dir = sort_dir,
            cryptocurrency_type = cryptocurrency_type,
            tag = tag,
            aux = aux
        )
        return LatestListing(response)._iterate()

    def quotes_latest(
        self,
        id =                                None,
        slug =                              None,
        symbol =                            None,
        convert =                           None,
        convert_id =                        None,
        aux =                               "num_market_pairs,cmc_rank,date_added,tags,platform,max_supply,circulating_supply,total_supply,is_active,is_fiat",
        skip_invalid =                      False
    ) -> LatestQuotes:

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
        return LatestQuotes(response)._iterate()

    def categories (
        self,
        start =                             1,
        limit =                             None,
        id =                                None,
        slug =                              None,
        symbol =                            None
    ) -> Categories:
        
        response = self._get (
            url = "/cryptocurrency/categories",
            start = start,
            limit = limit,
            id = id,
            slug = slug,
            symbol = symbol
        )
        return Categories(response)._iterate()

    def category (
        self,
        id,
        start =                             1,
        limit =                             100,
        convert =                           None,
        convert_id =                        None
    ) -> Category:

        response = self._get (
            url = "/cryptocurrency/category",
            id = id,
            start = start,
            limit = limit,
            convert = convert,
            convert_id = convert_id
        )
        return Category(response)._iterate()