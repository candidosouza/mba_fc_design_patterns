from abc import ABC, abstractmethod
from dataclasses import dataclass
from core.invoice.infra.database.database_adapter import DatabaseAdapter
from core.invoice.infra.database.postgres_adapter import ConnectionConfig, PostgresAdapter


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
        if db_config['db_type'] == "postgresql":
            postgres_config = ConnectionConfig(
                host=db_config['host'],
                port=db_config['port'],
                database=db_config['database'],
                user=db_config['user'],
                password=db_config['password']
            )
            return PostgresAdapter(postgres_config)
        elif db_config['db_type'] != "mysql":
            raise ValueError(f"Tipo de banco de dados não suportado: {db_config['db_type']}")


adapter_factory = ConcreteDatabaseAdapterFactory()

db_config = {
    'db_type': 'postgresql',
    'host': 'db',
    'port': '5432',
    'database': 'invoice',
    'user': 'postgres',
    'password': 'root'
}
postgres_adapter = adapter_factory.create_adapter(**db_config)
postgres_adapter.connect()
contracts_results = postgres_adapter.query("SELECT * FROM contract")
print(contracts_results)
postgres_adapter.close()
