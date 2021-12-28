from abc import abstractmethod


CUSTOM_NAME = "_cmcObject"

class _decorator:

    def __init__(self, iterator) -> None:
        self._iterator = iterator

    @abstractmethod
    def _iterate(self):
        pass     

class _list(_decorator):

    def __init__(self, iterator) -> None:
        super().__init__(iterator)

    def _iterate(self):
        atributes = []
        for item in self._iterator:
            value = item
            if type(value) == dict:
                value = _dict(value)._iterate()
            atributes.append(value)
        return atributes

class _dict(_decorator):

    def __init__(self, iterator) -> None:
        super().__init__(iterator)

    def _iterate(self):
        atributes = {}
        for key in self._iterator:
            value = self._iterator[key]
            if type(value) == dict:
                value = _dict(value)._iterate()
            elif type(value) == list:
                value = _list(value)._iterate()
            key = key if key.isidentifier() else "_" + key
            atributes[key] = value
        return type(CUSTOM_NAME, (), atributes)

class response(_dict):

    def __init__(self, response_text) -> None:
        self.status = _status()
        super().__init__(response_text)

class _status:

    timestamp = None
    error_code = None
    error_message = None
    elapsed = None
    credit_count = None