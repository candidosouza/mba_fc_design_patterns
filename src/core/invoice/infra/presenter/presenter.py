from dataclasses import dataclass
from typing import List
from core.invoice.application.usecase.dto import InvoicesOutput as Output
from core.invoice.application.presenter.presenter import Presenter


@dataclass(frozen=True)
class JsonPresenter(Presenter):

    def present(self, output: List[Output]):
        return output
    

@dataclass(frozen=True)
class CSVPresenter(Presenter):

    def present(self, output: List[Output]):
        line: str = [f'{data.date};{data.amount}' for data in output]
        return line
