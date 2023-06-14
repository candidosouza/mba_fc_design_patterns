from dataclasses import dataclass, field
from typing import Optional

from core.invoice.application.dto import InvoicesOutput
from core.invoice.application.repository.contract_repository import ContractRepository


@dataclass(slots=True, frozen=True)
class GenerateInvoices():

    contracts_repository: ContractRepository

    def execute(self, input_params: 'Input') -> 'Output':
        contracts_results = self.contracts_repository.list()
        output: InvoicesOutput = []
        for contract in contracts_results:
            invoices = contract.generate_invoices(
                input_params['month'], 
                input_params['year'], 
                input_params['type']
                )
            for invoice in invoices:
                output.append(GenerateInvoices.Output(
                    date=invoice.date,
                    amount=invoice.amount
                ))

        if 'format' not in input_params or input_params['format'] == 'json':
            return output
        if input_params['format'] == 'csv':
            line: str = [f'{invoice.date};{invoice.amount}' for invoice in output]
            return line
        raise Exception('Invalid format')

    @dataclass(slots=True, frozen=True)
    class Input:
        month: int
        year: int
        type: str
        format: Optional[str]

    @dataclass(slots=True, frozen=True)
    class Output(InvoicesOutput):
        pass




# from core.invoice.infra.repository.contract_database_repository import ContractDatabaseRepository
# from core.invoice.infra.repository.contract_in_memory_repository import ContractInMemoryRepository
# from core.invoice.infra.database.database_adapter_factory import ConcreteDatabaseAdapterFactory

# adapter_factory = ConcreteDatabaseAdapterFactory()
# db_config = {
#     'db_type': 'postgresql',
#     'host': 'db',
#     'port': '5432',
#     'database': 'invoice',
#     'user': 'postgres',
#     'password': 'root'
# }
# postgres_adapter = adapter_factory.create_adapter(**db_config)
# postgres_adapter.connect()

# input_parans = {
#     'month': 1,
#     'year': 2022,
#     'type': "cash"
# }
# contract = ContractDatabaseRepository(postgres_adapter)
# invoices = GenerateInvoices(contract)
# print('\n')
# print('database ##############################################')
# print(invoices.execute(input_parans))
# print('##############################################')
# print('\n')


# contract_in_memory_repository = ContractInMemoryRepository()
# invoices = GenerateInvoices(contract_in_memory_repository)
# print('\n')
# print('Memory ##############################################')
# print(invoices.execute(input_parans))
# print('##############################################')
# print('\n')