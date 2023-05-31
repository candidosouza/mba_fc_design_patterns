import psycopg2
from dataclasses import dataclass
from dateutil.relativedelta import relativedelta

from core.invoice.application.dto import InvoicesOutput
from core.invoice.application.repository.contract_repository import ContractRepository
from core.invoice.infra.repository.contract_database_repository import ContractDatabaseRepository


@dataclass(slots=True, frozen=True)
class GenerateInvoices:
    db_config = {
        'host': 'db',
        'port': '5432',
        'database': 'invoice',
        'user': 'postgres',
        'password': 'root'
    }

    def execute(self, input: 'Input') -> 'Output':
        contracts_repository = ContractDatabaseRepository()
        contracts_results, payment_results = contracts_repository.list()
        output: InvoicesOutput = []
        for contract in contracts_results:
            if input['type'] == 'cash':
                for payment in payment_results:
                    if payment[3].month + 1 != input['month'] or payment[3].year != input['year']:
                        output.append(GenerateInvoices.Output(
                            date=payment[3].strftime("%d/%m/%Y"),
                            amout=payment[2]
                        ))
            if input['type'] == 'accrual':
                period = 0
                while period <= contract[3]:
                    period+=1
                    date = contract[4] + relativedelta(months=period)
                    if date.month + 1 != input['month'] or date.year != input['year']:
                        amount = contract[2] / contract[3]
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

input_parans = {
    'month': 1,
    'year': 2022,
    'type': "cash"
}
GenerateInvoices().execute(input_parans)