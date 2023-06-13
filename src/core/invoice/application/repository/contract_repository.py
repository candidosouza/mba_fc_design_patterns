from abc import ABC
from ast import List

from core.invoice.domain.contract import Contract

CT = list[Contract]
class ContractRepository(ABC):
    
    def list(self) -> CT:
        raise NotImplementedError
    
    def create(self, items):
        raise NotImplementedError
