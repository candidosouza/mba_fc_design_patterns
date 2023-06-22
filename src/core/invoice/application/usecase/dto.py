from dataclasses import dataclass
from typing import Any


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


@dataclass(slots=True, frozen=True)
class MessageOutput:
    topic: str
    content: Any
