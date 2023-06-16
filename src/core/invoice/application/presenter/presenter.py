from abc import ABC
from typing import List
from core.invoice.application.dto import InvoicesOutput as Output

class Presenter(ABC):

    def present(self, output: List[Output]):
        raise NotImplementedError