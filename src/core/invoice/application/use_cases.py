import psycopg2
from dataclasses import dataclass
from dateutil.relativedelta import relativedelta

from core.invoice.application.dto import InvoicesOutput
from core.invoice.application.repository.contract_repository import ContractRepository


@dataclass(slots=True, frozen=True)
class GenerateInvoices():

    contracts_repository: ContractRepository

    def execute(self, input_params: 'Input') -> 'Output':
        contracts_results, payment_results = self.contracts_repository.list()
        output: InvoicesOutput = []
        for contract in contracts_results:
            if input_params['type'] == 'cash':
                for payment in payment_results:
                    if payment[3].month + 1 != input_params['month'] or payment[3].year != input_params['year']:
                        output.append(GenerateInvoices.Output(
                            date=payment[3].strftime("%d/%m/%Y"),
                            amout=payment[2]
                        ))
            if input_params['type'] == 'accrual':
                period = 0
                while period <= contract[3]:
                    period+=1
                    date = contract[4] + relativedelta(months=period)
                    if date.month + 1 != input_params['month'] or date.year != input_params['year']:
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
