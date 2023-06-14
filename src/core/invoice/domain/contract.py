from abc import ABC, abstractmethod
import datetime
from dataclasses import dataclass, field
from typing import Any, List, Optional
from dateutil.relativedelta import relativedelta
from core.invoice.domain.invoice import Invoice
from core.invoice.domain.payment import Payment
from core.shared.domain.entities import Entity


@dataclass(slots=True, kw_only=True, frozen=True)
class Contract(Entity):
    id_contract: str
    description: str
    amount: float
    periods: int
    date: Optional[datetime.datetime] = field(
        default_factory=lambda: datetime.datetime.now(datetime.timezone.utc)
    )
    payments: Optional[Payment] = field(default_factory=list)

    def add_payment(self, payment: Payment):
        self.payments.append(payment)
    
    def get_payments(self) -> List[Payment]:
        return self.payments
    
    def generate_invoices(self, mouth: int, year: int, type: str) -> List[Any]:
        invoice_generation_strategy = InvoiceGenerationFactory.create(type)
        return invoice_generation_strategy.generate(self, mouth, year)


class InvoiceGenerationFactory:
    @staticmethod
    def create(type: str):
        if type == 'accrual':
            return AccrualInvoiceGenerationStrategy()
        if type == 'cash':
            return CashInvoiceGenerationStrategy()
        raise Exception('Invalid invoice generation strategy')


class InvoiceGenerationStrategy(ABC):
    @abstractmethod
    def generate(self, contract: Contract, month: int, year: int) -> List[Invoice]:
        return NotImplemented


class CashInvoiceGenerationStrategy(InvoiceGenerationStrategy):
    def generate(self, contract: Contract, month: int, year: int) -> List[Invoice]:
        invoices: List[Invoice] = []
        for payment in contract.get_payments():
            if payment.date.month + 1 != month or payment.date.year != year:
                invoices.append(Invoice(
                    date=payment.date.strftime("%d/%m/%Y"),
                    amount=payment.amount
                ))
        return invoices


class AccrualInvoiceGenerationStrategy(InvoiceGenerationStrategy):
    def generate(self, contract: Contract, month: int, year: int) -> List[Invoice]:
        invoices: List[Invoice] = []
        period = 0
        while period <= contract.periods:
            period+=1
            date = contract.date + relativedelta(months=period)
            if date.month + 1 != month or date.year != year:
                amount = contract.amount / contract.periods
                invoices.append(Invoice(
                    date=date.strftime("%d/%m/%Y"),
                    amount=amount
                ))
        return invoices
