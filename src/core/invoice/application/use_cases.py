import psycopg2
from dataclasses import dataclass
from dateutil.relativedelta import relativedelta

from core.invoice.application.dto import InvoicesOutput
from core.invoice.application.repository.contract_repository import ContractRepository


@dataclass(slots=True, frozen=True)
class GenerateInvoices():

    contracts_repository: ContractRepository

    def execute(self, input_params: 'Input') -> 'Output':
        contracts_results = self.contracts_repository.list()
        output: InvoicesOutput = []
        for contract in contracts_results:
            if input_params['type'] == 'cash':
                for payment in contract.payments:
                    if payment.date.month + 1 != input_params['month'] or payment.date.year != input_params['year']:
                        output.append(GenerateInvoices.Output(
                            date=payment.date.strftime("%d/%m/%Y"),
                            amout=payment.amount
                        ))
            if input_params['type'] == 'accrual':
                period = 0
                while period <= contract.periods:
                    period+=1
                    date = contract.date + relativedelta(months=period)
                    if date.month + 1 != input_params['month'] or date.year != input_params['year']:
                        amount = contract.amount / contract.periods
                        output.append(GenerateInvoices.Output(
                            date=date.strftime("%d/%m/%Y"),
                            amout=amount
                        ))
            return output

    @dataclass(slots=True, frozen=True)
    class Input:
        month: int
        year: int
        type: str

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