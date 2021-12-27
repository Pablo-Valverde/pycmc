from typing import Iterator, SupportsIndex
import response


class Info(response.response):

    def __init__(self, resp) -> None:
        self.data = _data()
        super().__init__(resp)
        if not self._request_successful:
            raise RuntimeError(self.status.error_message)

class _crypto:

    def __init__(self) -> None:
        self.id = None
        self.name = None
        self.symbol = None
        self.category = None
        self.slug = None
        self.logo = None
        self.description = None
        self.date_added = None
        self.notice = None
        self.tags = None
        self.platform = _platform()
        self.urls = _urls()

class _data:

    def __init__(self) -> None:
        self.crypto_id_slug_symbol_address = _crypto()

class _platform:

    def __init__(self) -> None:
        self.id = None
        self.name = None
        self.symbol = None
        self.slug = None
        self.token_address = None

class _urls:

    def __init__(self) -> None:
        self.website = None
        self.technical_doc = None
        self.explorer = None
        self.source_code = None
        self.message_board = None
        self.chat = None
        self.announcement = None
        self.reddit = None
        self.twitter = None