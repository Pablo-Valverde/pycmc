from typing import SupportsIndex
import response


class LatestQuotes(response.response):

    def __init__(self, resp) -> None:
        self.data = _data()
        super().__init__(resp)

    def _iterate(self):
        currencies = self._iterator.pop("data")
        new_data = []
        for currency in currencies:
            new_data.append(currencies[currency])
        self._iterator["data"] = new_data
        return super()._iterate()

class _platform:

    id = None
    name = None
    symbol = None
    slug = None
    token_address = None

class _convert:

    price = None
    volume_24h = None
    volume_change_24h = None
    volume_24h_reported = None
    volume_7d = None
    volume_7d_reported = None
    volume_30d = None
    volume_30d_reported = None
    market_cap = None
    market_cap_dominance = None
    fully_diluted_market_cap = None
    percent_change_1h = None
    percent_change_24h = None
    percent_change_7d = None
    last_updated = None

class _quote:

    USD = _convert()

class _crypto:

    id = None
    name = None
    symbol = None
    slug = None
    is_active = None
    is_fiat = None
    cmc_rank = None
    cmc_rank = None
    circulating_supply = None
    total_supply = None
    market_cap_by_total_supply = None
    max_supply = None
    date_added = None
    tags = None
    platform = _platform()
    last_updated = None
    quote = _quote() 

class _data(list):

    def __getitem__(self, __i: SupportsIndex) -> _crypto:
        return _crypto()

    def pop(self, __index: SupportsIndex = ...) -> _crypto():
        return _crypto()
