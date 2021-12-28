import response


class Categories(response.response):

    def __init__(self, resp) -> None:
        self.data = _data()
        super().__init__(resp)

class _crypto:

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
    last_updated = None

class _data(list):

    def __getitem__(self, index) -> _crypto:
        return _crypto()

    def pop(self, __index) -> _crypto:
        return _crypto()
