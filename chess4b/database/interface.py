import aiosqlite
import asyncio

from chess4b.database.statements import CREATE_USER_TABLE, CREATE_GAMES_TABLE
from chess4b.models import User, Game


class SqlInterface:
    def __init__(self, db_file: str = "database.sqlite"):
        self._db: aiosqlite.Connection | None = None
        self.db_file: str = db_file

    async def setup(self) -> None:
        self._db = await aiosqlite.connect(self.db_file)
        await self.tables_setup()

    async def tables_setup(self) -> None:
        await self.execute(CREATE_USER_TABLE)
        await self.execute(CREATE_GAMES_TABLE)
        await self.commit()

    async def get_user_data(self, username: str) -> User:
        data = await self.execute("SELECT * FROM users WHERE username=?", username)
        return User(*await data.fetchone())

    async def execute(self, sql: str, *dta) -> aiosqlite.Cursor:
        return await self._db.execute(sql, *dta)

    async def commit(self) -> None:
        await self._db.commit()

    async def close(self) -> None:
        await self.commit()
        await self._db.close()


if __name__ == '__main__':
    intf = SqlInterface()
    loop = asyncio.new_event_loop()
    loop.run_until_complete(intf.setup())
