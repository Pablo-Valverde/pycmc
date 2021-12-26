from abc import abstractmethod
import json

REQUEST_SUCCESS = 200
BAD_REQUEST = 400
UNAUTHORIZED = 401
FORBIDDEN = 403
NOT_FOUND = 404
TOO_MANY_REQUESTS = 429
INTERNAL_SERVER_ERROR = 500

def _new_class(__name, __C):
    return type("_" + __name, (__C, ), {})()

class _decorator:

    @abstractmethod
    def iterate(self, iterable):
        pass     

class _list(_decorator, list):

    def __init__(self) -> None:
        super().__init__()

    def iterate(self, iterable):
        for item in iterable:
            value = item
            if type(item) == dict:
                value = _new_class("list_item", _dict)
                value.iterate(item)
            self.append(value)

class _dict(_decorator):

    def __init__(self) -> None:
        pass

    def iterate(self, iterable):
        for key in iterable:
            value = iterable[key]
            if type(iterable[key]) == dict:
                value = _new_class(key, _dict)
                value.iterate(iterable[key])
            elif type(iterable[key]) == list:
                value = _list()
                value.iterate(iterable[key])
            key = key if key.isidentifier() else "_" + key
            self.__setattr__(key, value)

class response(_dict):

    def __init__(self, resp) -> None:
        self.status = _status()
        self.__payload = json.loads(resp.text)
        self.iterate(self.__payload)
        self._response_http_code = resp.status_code
        self._request_successful = True if self._response_http_code == REQUEST_SUCCESS else False

class _status:

    def __init__(self) -> None:
        self.timestamp = None
        self.error_code = None
        self.error_message = None
        self.elapsed = None
        self.credit_count = None