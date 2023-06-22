from core.invoice.infra.kafka.kafka import KafkaConfig
from flask import Flask
from flask import request
from core.invoice.application.decorator.logger_decorator import LoggerDecorator
from core.invoice.application.usecase.generate_invoices import GenerateInvoices
from core.invoice.application.usecase.dto import EmailOutput, MessageOutput
from core.invoice.application.usecase.email_sender import EmailLogger, EmailSender
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
    email_logger = EmailLogger(mediator)
    email_sender = EmailSender(mediator)
    email_data = EmailOutput(
        sender="sender@example.com",
        recipient="recipient@example.com",
        subject="Hello",
        message="Hi, how are you?"
    )
    email_logger.handle_email_sent(email_data)
    email_sender.send(email_data)
    generate_invoices = LoggerDecorator(GenerateInvoices(contract_repository))
    output = generate_invoices.execute(request.args)
    kafka_config = KafkaConfig(bootstrap_servers="kafka:9092")
    message = kafka_config.Message(
        topic='invoices_generated',
        content=output
    )
    kafka_config.send(message)
    kafka_config.consume(['invoices_generated'], lambda data: print(data))
    if request.method == 'POST':
        output = generate_invoices.execute(request.form)
    return list(output)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
