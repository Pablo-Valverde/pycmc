from .. import response


class Info(response.response):

    def __init__(self, resp) -> None:
        self.data = _data()
        super().__init__(resp)

class _plan:

    credit_limit_daily = None
    credit_limit_daily_reset = None
    credit_limit_daily_reset_timestamp = None
    credit_limit_monthly = None
    credit_limit_monthly_reset = None
    credit_limit_monthly_reset_timestamp = None
    rate_limit_minute = None

class _current_minute:
    
    requests_made = None
    requests_left = None

class _current_day:
    
    credits_used = None
    credits_left = None

class _current_month:
    
    requests_made = None
    requests_left = None

class _usage:
    
    current_minute = _current_minute()
    current_day = _current_day()
    current_month = _current_month()

class _data:

    plan = _plan()
    usage = _usage()
