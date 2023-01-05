import socket
import asyncio


class LogicBase:
    def __init__(self, loop: asyncio.events.AbstractEventLoop = None, auto_start: bool = True):
        self.connection: socket.socket | None = None
        self.loop: asyncio.events.AbstractEventLoop = loop
        if auto_start:
            self._start()

    def _start(self):
        if not self.loop:
            self.loop = asyncio.new_event_loop()
