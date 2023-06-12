from abc import ABC


class ContractRepository(ABC):
    
    def list(self):
        raise NotImplementedError
    
    def create(self, items):
        raise NotImplementedError
