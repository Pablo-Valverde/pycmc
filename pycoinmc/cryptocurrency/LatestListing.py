from typing import SupportsIndex
from .. import response


class LatestListing(response.response):

    def __init__(self, resp) -> None:
        self.data = _data()
        super().__init__(resp)

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

class _platform:

    id = None
    name = None
    symbol = None
    slug = None
    token_address = None

class _crypto:

    id = None
    name = None
    symbol = None
    slug = None
    cmc_rank = None
    num_market_pairs = None
    circulating_supply = None
    total_supply = None
    market_cap_by_total_supply = None
    max_supply = None
    last_updated = None
    date_added = None
    tags = None
    platform = _platform()
    quote = _quote()

class _data(list):

    def __getitem__(self, __i: SupportsIndex) -> _crypto:
        return _crypto()

    def pop(self, __index: SupportsIndex = ...) -> _crypto():
        return _crypto()
