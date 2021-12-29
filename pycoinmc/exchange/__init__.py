import _cmcBranch

class exchangeAPI(_cmcBranch.cmcBranch):

    def __init__(self, __get) -> None:
        super().__init__(__get)

    def map(
        self,
        listing_status = None,
        slug = None,
        start = None,
        limit = None,
        sort = None,
        aux = None,
        crypto_id = None
    ):

        raise NotImplementedError()

    def info(
        self,
        id = None,
        slug = None,
        aux = None
    ):

        raise NotImplementedError()