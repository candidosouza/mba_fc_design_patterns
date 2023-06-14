import datetime
import unittest
from core.invoice.domain.contract import Contract
from core.invoice.domain.payment import Payment
from core.invoice.domain.invoice import Invoice

class TestContractIntegr(unittest.TestCase):

    def test_should_calculate_the_balance_of_the_contract(self):
        input_parans = {
            "id_contract": "123",
            "description": "Test",
            "amount": 6000,
            "periods": 12,
            "date": datetime.datetime.strptime("2022-01-01", '%Y-%m-%d').date()
        }
        contract = Contract(**input_parans)
        contract.add_payment(
            Payment(id_payment='123', id_contract='123', amount=2000, date=datetime.datetime.strptime("2022-01-01", '%Y-%m-%d').date())
        )
        self.assertEqual(contract.get_balance(), 4000)