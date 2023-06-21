from abc import ABC, abstractmethod


class Mediator(ABC):

    @abstractmethod
    def subscribe(event: str, callback: callable):
        return NotImplemented

    @abstractmethod
    def publish(event: str, data: dict):
        return NotImplemented
