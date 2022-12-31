import sqlite3

from chess4b.database.statements import CREATE_USER_TABLE, CREATE_GAMES_TABLE


class SqlInterface:
    def __init__(self, db_file: str = "database.sqlite", auto_setup: bool = True):
        self.db: sqlite3.Connection | None = None
        self.db_file: str = db_file
        if auto_setup:
            self.setup()

    def setup(self) -> None:
        self.db = sqlite3.connect(self.db_file)
        self.tables_setup()

    def tables_setup(self) -> None:
        self.execute(CREATE_USER_TABLE)
        self.execute(CREATE_GAMES_TABLE)
        self.commit()

    def execute(self, sql: str) -> sqlite3.Cursor:
        return self.db.execute(sql)

    def commit(self) -> None:
        self.db.commit()

    def close(self) -> None:
        self.commit()
        self.db.close()


if __name__ == '__main__':
    intf = SqlInterface()
