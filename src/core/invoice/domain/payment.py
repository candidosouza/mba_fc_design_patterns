

from dataclasses import dataclass
import datetime

from core.shared.domain.entities import Entity


@dataclass(slots=True, kw_only=True, frozen=True)
class Payment(Entity):
    id_payment: str
    id_contract: str
    amount: float
    date: datetime.datetime

