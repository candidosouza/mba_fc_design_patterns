import datetime
from dataclasses import dataclass, field
from typing import Optional

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
