import psycopg2
from dataclasses import dataclass
from core.invoice.application.repository.contract_repository import ContractRepository
from core.invoice.domain.contract import Contract
from core.invoice.domain.payment import Payment
from core.invoice.infra.database.database_adapter import DatabaseAdapter
from core.invoice.infra.database.database_adapter_factory import ConcreteDatabaseAdapterFactory


@dataclass(slots=True, frozen=True)
class ContractDatabaseRepository(ContractRepository):
    connection: DatabaseAdapter

    def list(self):
        try:
            contracts: Contract = []
            contracts_data = self.connection.query("SELECT * FROM contract")
            for contract_data in contracts_data:
                contract = Contract(
                    id_contract=contract_data[0],
                    description=contract_data[1],
                    amount=contract_data[2],
                    periods=contract_data[3],
                    date=contract_data[4]
                )
                payments_data =  self.connection.query(f"SELECT * FROM payment WHERE id_contract = '{str(contract.id_contract)}'")
                for payment_data in payments_data:
                    contract.payments.append(
                        Payment(
                            id_payment=payment_data[0],
                            id_contract=payment_data[1],
                            amount=payment_data[2],
                            date=payment_data[3]
                        )
                    )
                contracts.append(contract)
            return contracts
        except (Exception, psycopg2.Error) as error:
            print("Erro ao executar a consulta:", error)
        finally:
            self.connection.close()

    def create(self, items):
        pass
