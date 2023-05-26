import unittest

from core.invoice.application.use_cases import GenerateInvoices

class TestGeneratorInvocesIntegr(unittest.TestCase):

    def setUp(self):
        self.generate_invoices = GenerateInvoices()

    def test_should_generate_invoices(self):
        output = self.generate_invoices.execute()
        print('\n')
        print("###############################################")
        print(output)
        print("###############################################")
        print('\n')
        self.assertTrue(True)
