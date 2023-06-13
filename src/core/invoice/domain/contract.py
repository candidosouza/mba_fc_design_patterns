import datetime
from dataclasses import dataclass, field
from typing import Optional
from dateutil.relativedelta import relativedelta
from core.invoice.domain.invoice import Invoice

from core.shared.domain.entities import Entity
from core.invoice.domain.payment import Payment


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
    
    def get_payments(self):
        return self.payments
    
    def generate_invoices(self, mouth: int, year: int, type_transaction: str):
        invoices: Invoice = []
        if type_transaction == 'cash':
            for payment in self.get_payments():
                if payment.date.month + 1 != mouth or payment.date.year != year:
                    invoices.append(Invoice(
                        date=payment.date.strftime("%d/%m/%Y"),
                        amount=payment.amount
                    ))
        if type_transaction == 'accrual':
            period = 0
            while period <= self.periods:
                period+=1
                date = self.date + relativedelta(months=period)
                if date.month + 1 != mouth or date.year != year:
                    amount = self.amount / self.periods
                    invoices.append(Invoice(
                        date=date.strftime("%d/%m/%Y"),
                        amount=amount
                    ))
        return invoices
