from abc import ABC
from dataclasses import dataclass, field
import datetime
from typing import List

from core.invoice.application.repository.contract_repository import ContractRepository


@dataclass(slots=True, kw_only=True, frozen=True)
class ContractInMemoryRepository(ContractRepository, ABC):
    items: List = field(default_factory=list)

    def list(self) -> List:
        contracts_results = [
            (
                '4224a279-c162-4283-86f5-1095f559b08c',
                'Prestação de serviços escolares',
                6000,
                12,
                datetime.datetime(2022, 1, 1, 10, 0),
            )
        ]
        payment_results = [
            (
                'c931d9db-c8d8-44d4-8861-b3d6b734c64e',
                '4224a279-c162-4283-86f5-1095f559b08c',
                6000,
                datetime.datetime(2022, 1, 5, 10, 0)
            )
        ]

        return contracts_results, payment_results

    def create(self, items):
        self.items.append(items)
