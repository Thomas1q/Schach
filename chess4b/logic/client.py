from chess4b.logic import LogicBase


class LogicClient(LogicBase):
    @classmethod
    def from_selector(cls, obj):
        return cls()
