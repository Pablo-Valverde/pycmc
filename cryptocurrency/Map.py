import response

class Map(response.response):

    def __init__(self, resp) -> None:
        self.data = _data()
        super().__init__(resp)

class _platform:

    id = None
    name = None
    symbol = None
    slug = None
    token_address = None

class _crypto:

    id = None
    rank = None
    name = None
    symbol = None
    slug = None
    is_active = None
    first_historical_data = None
    last_historical_data = None
    platform = _platform()

class _data(list):

    def __getitem__(self, index) -> _crypto:
        return _crypto()

    def pop(self, __index) -> _crypto:
        return _crypto()