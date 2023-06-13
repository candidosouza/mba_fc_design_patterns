import unittest

from core.invoice.application.use_cases import GenerateInvoices
from core.invoice.infra.database.database_adapter_factory import ConcreteDatabaseAdapterFactory
from core.invoice.infra.repository.contract_in_memory_repository import ContractInMemoryRepository
from core.invoice.infra.repository.contract_database_repository import ContractDatabaseRepository

class TestGeneratorInvocesIntegr(unittest.TestCase):

    def setUp(self):
        self.adapter_factory = ConcreteDatabaseAdapterFactory()
        db_config = {
            'db_type': 'postgresql',
            'host': 'db',
            'port': '5432',
            'database': 'invoice',
            'user': 'postgres',
            'password': 'root'
        }
        self.postgres_adapter = self.adapter_factory.create_adapter(**db_config)
        self.postgres_adapter.connect()

        # self.contract_repository = ContractInMemoryRepository()
        # self.generate_invoices = GenerateInvoices(self.contract_repository) # pylint: disable=abstract-class-instantiated

        self.contract_repository = ContractDatabaseRepository(self.postgres_adapter)
        self.generate_invoices = GenerateInvoices(self.contract_repository) # pylint: disable=abstract-class-instantiated

    def tearDown(self) -> None:
        self.postgres_adapter.close()

    def test_should_generate_of_invoices_based_on_cash_basis_accounting(self):
        input_parans = {
            'month': 1,
            'year': 2022,
            'type': "cash"
        }
        output = self.generate_invoices.execute(input_parans)
        self.assertEqual(output[0].date, '05/01/2022')
        self.assertEqual(output[0].amount, 6000)

    def test_should_generate_of_invoices_based_on_accrual_basis_accounting(self):
        input_parans = {
            'month': 1,
            'year': 2022,
            'type': "accrual"
        }
        output = self.generate_invoices.execute(input_parans)
        self.assertEqual(output[0].date, '01/02/2022')
        self.assertEqual(output[0].amount, 500)

    def test_should_generate_of_invoices_based_on_accrual_basis_accounting_02(self):
        input_parans = {
            'month': 2,
            'year': 2022,
            'type': "accrual"
        }
        output = self.generate_invoices.execute(input_parans)
        self.assertEqual(output[0].date, '01/02/2022')
        self.assertEqual(output[0].amount, 500)
