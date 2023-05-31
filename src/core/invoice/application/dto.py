from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class InvoicesOutput:
    date: str
    amout: int
