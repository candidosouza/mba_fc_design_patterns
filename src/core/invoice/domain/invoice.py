import datetime
from dataclasses import dataclass
from core.shared.domain.entities import Entity


@dataclass(slots=True, kw_only=True, frozen=True)
class Invoice(Entity):
    date: datetime.datetime
    amount: float
    