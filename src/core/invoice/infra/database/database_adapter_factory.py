from abc import ABC, abstractmethod
from dataclasses import dataclass
from core.invoice.infra.database.database_adapter import DatabaseAdapter
from core.invoice.infra.database.type_database_adapter import (
    ConnectionConfig,
    PostgresAdapter,
    MySqlAdapter
)


@dataclass(slots=True, kw_only=True, frozen=True)
class DatabaseAdapterFactory(ABC):

    @staticmethod
    @abstractmethod
    def create_adapter(**db_config) -> DatabaseAdapter:
        pass


@dataclass(slots=True, kw_only=True, frozen=True)
class ConcreteDatabaseAdapterFactory(DatabaseAdapterFactory):

    @staticmethod
    def create_adapter(**db_config) -> DatabaseAdapter:
        config = ConnectionConfig(
            host=db_config['host'],
            port=db_config['port'],
            database=db_config['database'],
            user=db_config['user'],
            password=db_config['password']
        )
        if db_config['db_type'] == "postgresql":
            return PostgresAdapter(config)
        if db_config['db_type'] != "mysql":
            return MySqlAdapter(config)
        raise ValueError(f"Tipo de banco de dados não suportado: {db_config['db_type']}")