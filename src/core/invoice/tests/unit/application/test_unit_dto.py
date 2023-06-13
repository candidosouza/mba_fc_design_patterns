import unittest
from dataclasses import is_dataclass
from core.invoice.application.dto import InvoicesOutput


class TestInvoicesOutput(unittest.TestCase):

    def test_is_dataclass(self):
        self.assertTrue(is_dataclass(InvoicesOutput))
        self.assertTrue(InvoicesOutput.__dataclass_fields__)
        self.assertTrue(InvoicesOutput.__dataclass_params__)

    def test_fields(self):
        self.assertEqual(InvoicesOutput.__slots__, ('date', 'amount'))
        self.assertEqual(InvoicesOutput.__annotations__, {
            'date': str,
            'amount': int
        })
