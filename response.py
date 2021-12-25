import json

BAD_REQUEST = 400
UNAUTHORIZED = 401
FORBIDDEN = 403
TOO_MANY_REQUESTS = 429
INTERNAL_SERVER_ERROR = 500

class response:

    def __init__(self, resp) -> None:
        self.__payload = json.loads(resp.text)
        self.status = _status(self.__payload.pop("status"))
        self._response_http_code = resp.status_code
        self._request_successful = True if self.status.error_code == 0 else False

class _status:

    def __init__(self, status_dict:dict) -> None:
        self.timestamp = status_dict.pop("timestamp")
        self.error_code = status_dict.pop("error_code")
        self.error_message = status_dict.pop("error_message")
        self.elapsed = status_dict.pop("elapsed")
        self.credit_count = status_dict.pop("credit_count")
