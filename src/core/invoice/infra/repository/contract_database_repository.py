import psycopg2
from dataclasses import dataclass
from core.invoice.application.repository.contract_repository import ContractRepository
from core.invoice.infra.database.database_adapter import DatabaseAdapter
from core.invoice.infra.database.database_adapter_factory import ConcreteDatabaseAdapterFactory


@dataclass(slots=True, frozen=True)
class ContractDatabaseRepository(ContractRepository):
    connection: DatabaseAdapter

    def list(self):
        try:
            contracts_results = self.connection.query("SELECT * FROM contract")
            for contract in contracts_results:
                payment_results =  self.connection.query(f"SELECT * FROM payment WHERE id_contract = '{str(contract[0])}'")
            return contracts_results, payment_results
        except (Exception, psycopg2.Error) as error:
            print("Erro ao executar a consulta:", error)
        finally:
            self.connection.close()

    def create(self, items):
        pass

