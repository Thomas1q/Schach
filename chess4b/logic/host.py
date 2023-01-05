from chess4b.logic import LogicBase


class LogicHost(LogicBase):
    @classmethod
    def from_selector(cls, obj):
        return cls()
