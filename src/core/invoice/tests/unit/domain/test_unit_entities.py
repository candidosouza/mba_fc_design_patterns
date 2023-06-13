import datetime
import unittest
from dataclasses import FrozenInstanceError, is_dataclass

from core.invoice.domain.contract import Contract
from core.invoice.domain.payment import Payment
from core.invoice.domain.invoice import Invoice

class TestContractUnit(unittest.TestCase):

    def test_if_is_a_dataclass(self):
        self.assertTrue(is_dataclass(Contract))

    def test_initialization_contract(self):
        data = {
            "id_contract": "123",
            "description": "Test",
            "amount": 100.0,
            "periods": 1,
            "date": "2021-01-01T00:00:00+00:00",
            "payments": []
        }
        contract = Contract(**data)
        self.assertEqual(contract.id_contract, data["id_contract"])
        self.assertEqual(contract.description, data["description"])
        self.assertEqual(contract.amount, data["amount"])
        self.assertEqual(contract.periods, data["periods"])
        self.assertEqual(contract.date, data["date"])
        self.assertEqual(contract.payments, data["payments"])


class TestPaymentUnit(unittest.TestCase):

    def test_if_is_a_dataclass(self):
        self.assertTrue(is_dataclass(Payment))

    def test_initialization_payment(self):
        data = {
            "id_payment": "123",
            "id_contract": "123",
            "amount": 100.0,
            "date": "2021-01-01T00:00:00+00:00",
        }
        payment = Payment(**data)
        self.assertEqual(payment.id_payment, data["id_payment"])
        self.assertEqual(payment.id_contract, data["id_contract"])
        self.assertEqual(payment.amount, data["amount"])
        self.assertEqual(payment.date, data["date"])


class TestInvoiceUnit(unittest.TestCase):

    def test_if_is_a_dataclass(self):
        self.assertTrue(is_dataclass(Invoice))

    def test_initialization_invoice(self):
        data = {
            "amount": 100.0,
            "date": "2021-01-01T00:00:00+00:00",
        }
        invoice = Invoice(**data)
        self.assertEqual(invoice.amount, data["amount"])
        self.assertEqual(invoice.date, data["date"])

    def test_should_generate_invoices_from_a_contract(self):
        input_parans = {
            "id_contract": "123",
            "description": "Test",
            "amount": 6000,
            "periods": 12,
            "date": datetime.datetime.strptime("2022-01-01", '%Y-%m-%d').date()
        }
        contract = Contract(**input_parans)
        invoices = contract.generate_invoices(1, 2022, 'accrual')
        self.assertEqual(invoices[0].date, '01/02/2022')
        self.assertEqual(invoices[0].amount, 500)