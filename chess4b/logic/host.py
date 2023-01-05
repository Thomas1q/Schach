import asyncio
from chess4b.logic import LogicBase, HostClientSelector
from chess4b.network import Server
from chess4b.database import SqlInterface
from chess4b.models import User, Game


class LogicHost(LogicBase):
    def __init__(self, loop: asyncio.events.AbstractEventLoop, username: str):
        super().__init__(loop, False, False)

        self._host_server: asyncio.AbstractServer | None = None
        self._db_interface: SqlInterface = SqlInterface()

        self.user_data: User | None = None
        self.enemy_data: User | None = None

        self.setup(username)

        self.screen: pygame.Surface | None = None
        self.event_queue: asyncio.Queue = asyncio.Queue()

    def setup(self, username: str):
        self.loop.call_soon(self.resolve_user_database, username)

    async def resolve_user_database(self, user_name: str):
        self.user_data = await self._db_interface.get_user_data(user_name)

    async def resolve_enemy_database(self, enemy_name: str):
        self.enemy_data = await self._db_interface.get_user_data(enemy_name)

    @classmethod
    def from_selector(cls, sel: HostClientSelector):
        return cls(sel.loop, sel.username)
