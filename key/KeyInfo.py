import response


class InvalidKey(Exception):

    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class KeyInfo(response.response):

    def __init__(self, resp) -> None:
        super().__init__(resp)
        if self._response_http_code == response.UNAUTHORIZED:
            raise InvalidKey(self.status.error_message)
        elif not self._request_successful:
            raise RuntimeError(self.status.error_message)
        self.data = _data(self._response__payload.pop("data"))

class _data:

    def __init__(self, data_dict:dict) -> None:
        self.plan = _plan(data_dict.pop("plan"))
        self.usage = _usage(data_dict.pop("usage"))

class _plan:

    def __init__(self, plan_dict:dict) -> None:
        self.credit_limit_daily = plan_dict.pop("credit_limit_daily")
        self.credit_limit_daily_reset = plan_dict.pop("credit_limit_daily_reset")
        self.credit_limit_daily_reset_timestamp = plan_dict.pop("credit_limit_daily_reset_timestamp")
        self.credit_limit_monthly = plan_dict.pop("credit_limit_monthly")
        self.credit_limit_monthly_reset = plan_dict.pop("credit_limit_monthly_reset")
        self.credit_limit_monthly_reset_timestamp = plan_dict.pop("credit_limit_monthly_reset_timestamp")
        self.rate_limit_minute = plan_dict.pop("rate_limit_minute")

class _usage:
    
    def __init__(self, usage_dict:dict) -> None:
        self.current_minute = _current_minute(usage_dict.pop("current_minute"))
        self.current_day = _current_day(usage_dict.pop("current_day"))
        self.current_month = _current_month(usage_dict.pop("current_month"))

class _current_minute:
    
    def __init__(self, current_minute_dict:dict) -> None:
        self.requests_made = current_minute_dict.pop("requests_made")
        self.requests_left = current_minute_dict.pop("requests_left")

class _current_day:
    
    def __init__(self, current_day_dict:dict) -> None:
        self.credits_used = current_day_dict.pop("credits_used")
        self.credits_left = current_day_dict.pop("credits_left")

class _current_month:
    
    def __init__(self, current_month_dict:dict) -> None:
        self.requests_made = current_month_dict.pop("credits_used")
        self.requests_left = current_month_dict.pop("credits_left")
