import logging

from random import randint

import aiosqlite

from application.encoder import encode
from application.encoder import decode


_create_table_query = '''
CREATE TABLE IF NOT EXISTS storage
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    salt INTGER,
    url TEXT UNIQUE
)
'''

_insert_query = '''
INSERT INTO storage (salt, url) VALUES (:salt, :url) RETURNING id
'''

_search_by_id_query = '''
SELECT id, salt, url FROM storage WHERE id = :id
'''

_search_by_url_query = '''
SELECT id, salt, url FROM storage WHERE url = :url
'''


class TokenNotFoundError(Exception):
    pass


class SqliteStorage:
    db_filename = 'storage.db'
    salt_limit = 1000

    async def configure(self) -> None:
        async with aiosqlite.connect(self.db_filename) as connection:
            await connection.execute(_create_table_query)
            await connection.commit()
    
    async def store(self, url: str) -> str:
        async with aiosqlite.connect(self.db_filename) as connection:
            connection.row_factory = aiosqlite.Row
            async with connection.execute(_search_by_url_query, {"url": url}) as cursor:
                row = await cursor.fetchone()
                if row is not None:
                    logging.info(f'Exists ({row["id"]}, {row["salt"]}, {row["url"]})')
                    return encode(row['id'] * self.salt_limit + row['salt'])

        salt = randint(0, self.salt_limit - 1)

        async with aiosqlite.connect(self.db_filename) as connection:
            async with connection.execute(_insert_query, {"salt": salt, "url": url}) as cursor:
                (id_, ) = await cursor.fetchone()
            await connection.commit()

        logging.info(f'Store ({id_}, {salt}, {url})')
        return encode(id_ * self.salt_limit + salt)

    async def retrieve(self, token: str) -> str:
        id_ = decode(value=token) // self.salt_limit

        async with aiosqlite.connect(self.db_filename) as connection:
            connection.row_factory = aiosqlite.Row
            async with connection.execute(_search_by_id_query, {"id": id_}) as cursor:
                row = await cursor.fetchone()
                if row is None:
                    logging.info(f'Token "{token}" not found; Calculated ID = {id_}')
                    raise TokenNotFoundError(f'Token "{token}" not found in storage')
                logging.info(f'Load ({row['id']}, {row['salt']}, {row['url']})')
                return row['url']


storage = SqliteStorage()
