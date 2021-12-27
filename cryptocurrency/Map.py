import response

class Map(response.response):

    def __init__(self, resp) -> None:
        self.data = []
        super().__init__(resp)
        if not self._request_successful:
            raise RuntimeError(self.status.error_message)
