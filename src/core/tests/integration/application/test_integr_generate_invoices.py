import unittest

from core.invoice.application.use_cases import GenerateInvoices
from core.invoice.infra.repository.contract_database_repository import ContractDatabaseRepository

class TestGeneratorInvocesIntegr(unittest.TestCase):

    def setUp(self):
        self.contract_repository = ContractDatabaseRepository()
        self.generate_invoices = GenerateInvoices(self.contract_repository) # pylint: disable=abstract-class-instantiated

    def test_should_generate_of_invoices_based_on_cash_basis_accounting(self):
        input_parans = {
            'month': 1,
            'year': 2022,
            'type': "cash"
        }
        output = self.generate_invoices.execute(input_parans)
        self.assertEqual(output[0].date, '05/01/2022')
        self.assertEqual(output[0].amout, 6000)

    def test_should_generate_of_invoices_based_on_accrual_basis_accounting(self):
        input_parans = {
            'month': 1,
            'year': 2022,
            'type': "accrual"
        }
        output = self.generate_invoices.execute(input_parans)
        self.assertEqual(output[0].date, '01/02/2022')
        self.assertEqual(output[0].amout, 500)

    def test_should_generate_of_invoices_based_on_accrual_basis_accounting_02(self):
        input_parans = {
            'month': 2,
            'year': 2022,
            'type': "accrual"
        }
        output = self.generate_invoices.execute(input_parans)
        self.assertEqual(output[0].date, '01/02/2022')
        self.assertEqual(output[0].amout, 500)
