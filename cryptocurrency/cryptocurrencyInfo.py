from typing import Iterator, SupportsIndex
import response


class crypInfo(response.response):

    def __init__(self, resp) -> None:
        super().__init__(resp)
        if not self._request_successful:
            raise RuntimeError(self.status.error_message)
        self.data = _data(self._response__payload.pop("data"))

class _crypto:

    def __init__(self, crypto_dict:dict) -> None:
        self.id = crypto_dict.get("id")
        self.name = crypto_dict.get("name")
        self.symbol = crypto_dict.get("symbol")
        self.category = crypto_dict.get("category")
        self.slug = crypto_dict.get("slug")
        self.logo = crypto_dict.get("logo")
        self.description = crypto_dict.get("description")
        self.date_added = crypto_dict.get("date_added")
        self.notice = crypto_dict.get("notice")
        self.tags = crypto_dict.get("tags")
        platform_dict = crypto_dict.get("platform")
        self.platform = _platform(platform_dict) if platform_dict else None
        self.urls = _urls(crypto_dict.get("urls"))

class _data:

    def __init__(self, data_dict:dict) -> None:
        self.cryptocurrencies = [_crypto(data_dict[cryptoData]) for cryptoData in data_dict]

    def __getitem__(self, __i: SupportsIndex) -> _crypto:
        return self.cryptocurrencies[__i]

    def __iter__(self) -> Iterator[_crypto]:
        return self.cryptocurrencies.__iter__()

class _platform:

    def __init__(self, platform_dict:dict) -> None:
        self.id = platform_dict.get("id")
        self.name = platform_dict.get("name")
        self.symbol = platform_dict.get("symbol")
        self.slug = platform_dict.get("slug")
        self.token_address = platform_dict.get("token_address")

class _urls:

    def __init__(self, urls_dict:dict) -> None:
        self.website = urls_dict.get("website")
        self.technical_doc = urls_dict.get("technical_doc")
        self.explorer = urls_dict.get("explorer")
        self.source_code = urls_dict.get("source_code")
        self.message_board = urls_dict.get("message_board")
        self.chat = urls_dict.get("chat")
        self.announcement = urls_dict.get("announcement")
        self.reddit = urls_dict.get("reddit")
        self.twitter = urls_dict.get("twitter")