
CREATE_USER_TABLE = """
create table if not exists users
(
    user_id  integer
        constraint users_pk
            primary key autoincrement,
    username text,
    wins     integer default 0
);"""

CREATE_GAMES_TABLE = """
create table if not exists games
(
    game_id integer
        constraint games_pk
            primary key autoincrement,
    black   integer
        constraint games_black
            references users (user_id),
    white   integer
        constraint games_white
            references users (user_id),
    started timestamp default current_timestamp,
    ended   timestamp
);"""
