from dataclasses import dataclass, field
from typing import Optional

from core.invoice.application.usecase.dto import EmailOutput, InvoicesOutput
from core.invoice.application.presenter.presenter import Presenter
from core.invoice.application.repository.contract_repository import ContractRepository
from core.invoice.application.usecase.email_sender import EmailLogger, EmailSender
from core.invoice.application.usecase.use_case import UseCase
from core.invoice.infra.mediator.mediator import Mediator
from core.invoice.infra.presenter.presenter import CSVPresenter, JsonPresenter


@dataclass(slots=True, frozen=True)
class GenerateInvoices(UseCase):

    contracts_repository: ContractRepository
    presenter: Presenter = field(default_factory=lambda : JsonPresenter())
    mediator: Mediator = field(default_factory=lambda : Mediator)

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
        self.mediator.publish(event='invoices_generated', data=output)
        email_logger = EmailLogger(self.mediator)
        email_sender = EmailSender(self.mediator)
        email_data = EmailOutput(
            sender="sender@example.com",
            recipient="recipient@example.com",
            subject="Hello",
            message="Hi, how are you?"
        )
        email_logger.handle_email_sent(email_data)
        email_sender.send(email_data)
        return self.presenter.present(output)
        

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