import json

BAD_REQUEST = 400
UNAUTHORIZED = 401
FORBIDDEN = 403
TOO_MANY_REQUESTS = 429
INTERNAL_SERVER_ERROR = 500

class _data_decorator:

    def __init__(self) -> None:
        pass

    def iteratecmcDict(self, cmcdict):
        for key in cmcdict:
            value = cmcdict[key]
            if type(cmcdict[key]) == dict:
                value = _data_decorator.__new_class(key)()
                value.iteratecmcDict(cmcdict[key])
            self.__setattr__(key, value)

    @staticmethod
    def __new_class(name):
        return type("_" + name, (_data_decorator, ), {})

class response(_data_decorator):

    def __init__(self, resp) -> None:
        self.status = _status()
        self.__payload = json.loads(resp.text)
        self.iteratecmcDict(self.__payload)
        self._response_http_code = resp.status_code
        self._request_successful = True if self.status.error_code == 0 else False

class _status:

    def __init__(self) -> None:
        self.timestamp = None
        self.error_code = None
        self.error_message = None
        self.elapsed = None
        self.credit_count = None