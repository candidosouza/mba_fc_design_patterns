from abc import ABC
from dataclasses import dataclass
from typing import List

from core.invoice.application.repository.contract_repository import ContractRepository


@dataclass(slots=True, frozen=True)
class ContractInMemoryRepository:
    items: List = []

    def list(self) -> List:
      return self.items

    def create(self, items):
        self.items.append(items)


input_parans = {
    'month': 1,
    'year': 2022,
    'type': "cash"
}
contract = ContractInMemoryRepository()
contract.create(input_parans)
payment_results = contract.list()
print(payment_results)
