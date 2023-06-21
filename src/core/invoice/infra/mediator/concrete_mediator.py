from dataclasses import dataclass, field
from re import sub
from typing import Any
from core.invoice.infra.mediator.mediator import Mediator


@dataclass(slots=True, frozen=True)
class ConcreteMediator(Mediator):
    subscribers: dict = field(default_factory=dict)

    def publish(self, event: str, data: Any):
        if event in self.subscribers:
            for subscriber in self.subscribers[event]:
                subscriber(data)

    def subscribe(self, event: str, callback: callable):
        if event not in self.subscribers:
            self.subscribers[event] = []
        self.subscribers[event].append(callback)
