from core.invoice.application.usecase.dto import EmailOutput
from core.invoice.application.usecase.email_sender import EmailLogger, EmailSender
from flask import Flask
from flask import request
from core.invoice.application.decorator.logger_decorator import LoggerDecorator
from core.invoice.application.usecase.generate_invoices import GenerateInvoices
from core.invoice.infra.database.database_adapter_factory import ConcreteDatabaseAdapterFactory
from core.invoice.infra.repository.contract_database_repository import ContractDatabaseRepository
from core.invoice.infra.mediator.concrete_mediator import ConcreteMediator

app = Flask(__name__)


@app.route("/generate_invoices/", methods=['GET', 'POST'])
def generate_invoices():
    db_config = {
        'db_type': 'postgresql',
        'host': 'db',
        'port': '5432',
        'database': 'invoice',
        'user': 'postgres',
        'password': 'root'
    }
    adapter_factory = ConcreteDatabaseAdapterFactory()
    postgres_adapter = adapter_factory.create_adapter(**db_config)
    postgres_adapter.connect()
    contract_repository = ContractDatabaseRepository(postgres_adapter)
    mediator = ConcreteMediator()
    mediator.subscribe('invoices_generated', lambda data: print(data))
    generate_invoices = LoggerDecorator(GenerateInvoices(contract_repository))
    output = generate_invoices.execute(request.args)
    if request.method == 'POST':
        output = generate_invoices.execute(request.form)
    return list(output)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
