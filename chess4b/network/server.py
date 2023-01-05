import asyncio

from chess4b.network import Client


class Server(Client):
    def __init__(self, server: asyncio.AbstractServer = None):
        self.server: asyncio.Server = server
        super().__init__()

    async def start_server(self, host: str = "127.0.0.1", port: int = 50000):
        await asyncio.start_server(self.new_connection, host, port)
        async with self.server:
            await self.server.serve_forever()

    async def new_connection(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
        self.reader = reader
        self.writer = writer
        await self.server.wait_closed()
