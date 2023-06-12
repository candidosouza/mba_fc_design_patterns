import datetime
import uuid
from abc import ABC
from dataclasses import dataclass, field

from typing import List

from core.invoice.application.repository.contract_repository import ContractRepository


@dataclass(slots=True, kw_only=True, frozen=True)
class ContractInMemoryRepository(ContractRepository, ABC):
    items: List = field(default_factory=list)

    def list(self) -> List:
        id_contract = str(uuid.uuid4())
        id_payment = str(uuid.uuid4())
        contracts_results = [
            (
                id_contract,
                'Prestação de serviços escolares',
                6000,
                12,
                datetime.datetime(2022, 1, 1, 10, 0),
            )
        ]
        payment_results = [
            (
                id_contract,
                id_payment,
                6000,
                datetime.datetime(2022, 1, 5, 10, 0)
            )
        ]

        return contracts_results, payment_results
        # return self.items

    def create(self, items):
        self.items.append(items)

