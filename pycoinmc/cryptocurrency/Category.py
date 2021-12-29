import response


class Category(response.response):

    def __init__(self, resp) -> None:
        self.data = _data()
        super().__init__(resp)

class _platform:

    id = None
    name = None
    symbol = None
    slug = None
    token_address = None

class _convert:

    price = None
    volume_24h = None
    volume_24h_reported = None
    volume_7d = None
    volume_7d_reported = None
    volume_30d = None
    volume_30d_reported = None
    market_cap = None
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
    cmc_rank = None
    num_market_pairs = None
    circulating_supply = None
    total_supply = None
    max_supply = None
    last_updated = None
    date_added = None
    tags = None
    platform = _platform()
    quote = _quote()

class _coins(list):

    def __getitem__(self, index) -> _crypto:
        return _crypto()

    def pop(self, __index) -> _crypto:
        return _crypto()


class _data:

    id = None
    name = None
    title = None
    description = None
    num_tokens = None
    avg_price_change = None
    market_cap = None
    market_cap_change = None
    volume = None
    volume_change = None
    coins = _coins()