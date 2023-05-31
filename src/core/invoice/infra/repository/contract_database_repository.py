import psycopg2

from core.invoice.application.repository.contract_repository import ContractRepository


class ContractDatabaseRepository(ContractRepository):
    db_config = {
        'host': 'db',
        'port': '5432',
        'database': 'invoice',
        'user': 'postgres',
        'password': 'root'
    }

    def list(self):
        connection = None
        try:
            connection = psycopg2.connect(**self.db_config)
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM contract")
            contracts_results = cursor.fetchall()
            for contract in contracts_results:
                cursor.execute(f"SELECT * FROM payment WHERE id_contract = '{str(contract[0])}'")
                payment_results = cursor.fetchall()
            return contracts_results, payment_results
        except (Exception, psycopg2.Error) as error:
            print("Erro ao executar a consulta:", error)
        finally:
            if connection:
                cursor.close()
                connection.close()


contract = ContractDatabaseRepository()
contracts_results, payment_results = contract.list()
print(contracts_results)
print(payment_results)
