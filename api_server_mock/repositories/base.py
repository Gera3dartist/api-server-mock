from asyncpg.connection import Connection

class BaseRespository:
    def __init__(self, connection: Connection) -> None:
        self._conn = connection
    
    @property
    def connection(self) -> Connection:
        return self._conn
