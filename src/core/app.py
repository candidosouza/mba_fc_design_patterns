from flask import Flask
from flask import request
from core.invoice.application.decorator.logger_decorator import LoggerDecorator
from core.invoice.application.usecase.generate_invoices import GenerateInvoices
from core.invoice.infra.database.database_adapter_factory import ConcreteDatabaseAdapterFactory
from core.invoice.infra.repository.contract_database_repository import ContractDatabaseRepository

app = Flask(__name__)


@app.route("/generate_invoices", methods=['GET', 'POST'])
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
    generate_invoices = LoggerDecorator(GenerateInvoices(contract_repository))
    input_parans = {
        'month': request.args.get('month'),
        'year': request.args.get('year'),
        'type': request.args.get('type'),
        'user_agent': request.headers.get('User-Agent')
    }
    output = generate_invoices.execute(input_parans)
    if request.method == 'POST':
        input_parans = {
            'month': request.form['month'],
            'year': request.form['year'],
            'type': request.form['type'],
            'user_agent': request.headers.get('User-Agent')
        }
        output = generate_invoices.execute(input_parans)
    return list(output)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
