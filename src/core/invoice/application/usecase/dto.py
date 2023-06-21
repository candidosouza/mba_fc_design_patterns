from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class InvoicesOutput:
    date: str
    amount: int


@dataclass(slots=True, frozen=True)
class EmailOutput:
    sender: str
    recipient: str
    subject: str
    message: str
