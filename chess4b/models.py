import datetime
from dataclasses import dataclass


@dataclass
class User:
    user_id: int
    username: str
    wins: int


@dataclass
class Game:
    game_id: int
    black: User
    white: User
    started: datetime.datetime
    ended: datetime.datetime
