import aiosqlite
import asyncio

from chess4b.database.statements import CREATE_USER_TABLE, CREATE_GAMES_TABLE


class SqlInterface:
    def __init__(self, db_file: str = "database.sqlite"):
        self._db: aiosqlite.Connection | None = None
        self.db_file: str = db_file

    async def setup(self) -> None:
        self._db = await aiosqlite.connect(self.db_file)
        print(self._db)
        await self.tables_setup()

    async def tables_setup(self) -> None:
        print("setup")
        await self.execute(CREATE_USER_TABLE)
        print("user_table")
        await self.execute(CREATE_GAMES_TABLE)
        print("games_table")
        await self.commit()
        print("commit")

    async def execute(self, sql: str) -> aiosqlite.Cursor:
        return await self._db.execute(sql)

    async def commit(self) -> None:
        await self._db.commit()

    async def close(self) -> None:
        await self.commit()
        await self._db.close()


if __name__ == '__main__':
    intf = SqlInterface()
    loop = asyncio.new_event_loop()
    loop.run_until_complete(intf.setup())
