from abc import ABC
from dataclasses import dataclass

@dataclass(slots=True, frozen=True)
class UseCase(ABC):
    def execute(self, input_params: 'Input') -> 'Output':
        raise NotImplementedError()