import response


class InvalidKey(Exception):

    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class Info(response.response):

    def __init__(self, resp) -> None:
        self.data = _data()
        super().__init__(resp)
        if self._response_http_code == response.UNAUTHORIZED:
            raise InvalidKey(self.status.error_message)
        elif not self._request_successful:
            raise RuntimeError(self.status.error_message)

class _data:

    def __init__(self) -> None:
        self.plan = _plan()
        self.usage = _usage()

class _plan:

    def __init__(self) -> None:
        self.credit_limit_daily = None
        self.credit_limit_daily_reset = None
        self.credit_limit_daily_reset_timestamp = None
        self.credit_limit_monthly = None
        self.credit_limit_monthly_reset = None
        self.credit_limit_monthly_reset_timestamp = None
        self.rate_limit_minute = None

class _usage:
    
    def __init__(self) -> None:
        self.current_minute = _current_minute()
        self.current_day = _current_day()
        self.current_month = _current_month()

class _current_minute:
    
    def __init__(self) -> None:
        self.requests_made = None
        self.requests_left = None

class _current_day:
    
    def __init__(self) -> None:
        self.credits_used = None
        self.credits_left = None

class _current_month:
    
    def __init__(self) -> None:
        self.requests_made = None
        self.requests_left = None
