from abc import ABC
from dataclasses import dataclass, field
from core.shared.domain.value_objects import UniqueEntityId


@dataclass(frozen=True, slots=True)
class Entity(ABC):

    unique_entity_id: UniqueEntityId = field(
        default_factory=lambda: UniqueEntityId()  # pylint: disable=unnecessary-lambda
    )

    @property
    def id(self):  # pylint: disable=invalid-name
        return str(self.unique_entity_id)
