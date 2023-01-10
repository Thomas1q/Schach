import sqlite3
import asyncio

from chess4b.database.statements import CREATE_USER_TABLE, CREATE_GAMES_TABLE
from chess4b.models import User, Game


class SqlInterface:
    def __init__(self, db_file: str = "database.sqlite"):
        self._db: sqlite3.Connection | None = None
        self.db_file: str = db_file

    def setup(self, tables: bool = True) -> None:
        self._db = sqlite3.connect(self.db_file)
        self.tables_setup()

    def tables_setup(self) -> None:
        self.execute(CREATE_USER_TABLE)
        self.execute(CREATE_GAMES_TABLE)
        self.commit()

    def get_user_data(self, username: str) -> User | None:
        data = self.execute("SELECT * FROM users WHERE username=?", (username, ))
        user = data.fetchone()
        if not user:
            data = self.execute("INSERT INTO users (username) VALUES (?) RETURNING *", (username, ))
            user = data.fetchone()
        return User(*user)

    def execute(self, sql: str, *dta) -> sqlite3.Cursor:
        return self._db.execute(sql, *dta)

    def commit(self) -> None:
        self._db.commit()

    def close(self) -> None:
        self.commit()
        self._db.close()


if __name__ == '__main__':
    intf = SqlInterface()
    intf.setup()
