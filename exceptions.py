class TLLException(Exception):
    ...


class NotEnoughVariables(TLLException):
    def __init__(self):
        super(NotEnoughVariables, self).__init__('NotEnoughVariables')
