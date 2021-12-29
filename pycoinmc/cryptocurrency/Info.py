from .. import response


class Info(response.response):

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


class _urls:

    website = None
    technical_doc = None
    explorer = None
    source_code = None
    message_board = None
    chat = None
    announcement = None
    reddit = None
    twitter = None

class _crypto:

    id = None
    name = None
    symbol = None
    category = None
    slug = None
    logo = None
    description = None
    date_added = None
    notice = None
    tags = None
    platform = _platform()
    urls = _urls()

class _data(list):

    def __getitem__(self, index) -> _crypto:
        return _crypto()

    def pop(self, __index) -> _crypto:
        return _crypto()
