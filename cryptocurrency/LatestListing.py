from typing import Iterator, SupportsIndex
import response


class LatestListing(response.response):

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
        self.slug = crypto_dict.get("slug")
        #self.is_active = crypto_dict.get("is_active")
        #self.status = crypto_dict.get("status")
        #self.first_historical_data = crypto_dict.get("first_historical_data")
        #self.last_historical_data = crypto_dict.get("last_historical_data")
        self.tags = crypto_dict.get("tags")
        platform_dict = crypto_dict.get("platform")
        self.platform = _platform(platform_dict) if platform_dict else None

class _data:

    def __init__(self, data_dict:dict) -> None:
        self.cryptocurrencies = [_crypto(cryptoData) for cryptoData in data_dict]

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
