import _cmcBranch
from key.Info import Info

class keyAPI(_cmcBranch.cmcBranch):

    def __init__(self, __get) -> None:
        super().__init__(__get)

    def info (
        self
    ) -> Info:

        response = self._get (
            url = "/key/info"
        )
        return Info(response)