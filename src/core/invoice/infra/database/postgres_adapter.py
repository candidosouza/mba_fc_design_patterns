from dataclasses import dataclass, field
import psycopg2
from core.invoice.infra.database.database_adapter import DatabaseAdapter


@dataclass
class ConnectionConfig:
    host: str
    port: str
    database: str
    user: str
    password: str


class PostgresAdapter(DatabaseAdapter):

    def __init__(self, config: ConnectionConfig):
        self.config = config
        self.connection = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                host=self.config.host,
                port=self.config.port,
                database=self.config.database,
                user=self.config.user,
                password=self.config.password
            )
            print("Connection to PostgreSQL DB successful")
        except (Exception, psycopg2.Error) as error: # pylint: disable=broad-exception-caught
            print("Error while connecting to PostgreSQL", error)
            raise error

    def query(self, query: str):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            return cursor.fetchall()
        except (Exception, psycopg2.Error) as error: # pylint: disable=broad-exception-caught
            print("Error while executing query", error)

    def close(self):
        if self.connection:
            self.connection.close()
            print("PostgreSQL connection is closed")
