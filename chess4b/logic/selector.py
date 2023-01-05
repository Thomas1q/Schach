import asyncio

from chess4b.logic import LogicBase, LogicHost, LogicClient
from chess4b.ui import LoginPage


class HostClientSelector(LogicBase):
    def __init__(self, loop: asyncio.events.AbstractEventLoop = None, auto_start: bool = True, auto_run: bool = True):
        self.username: str | None = None

        super().__init__(loop, auto_start, auto_run)
        self.loop.call_soon_threadsafe(self.login)

    async def login(self):
        lp = LoginPage()
        self.username = await lp.get_login()

        host = await lp.check_host()
        if host:
            LogicHost.from_selector(self)
        else:
            LogicClient.from_selector(self)




