from abc import ABC, abstractmethod


class DatabaseAdapter(ABC):

    def connect(self):
        return NotImplementedError

    def query(self, query: str):
        return NotImplementedError

    def close(self):
        return NotImplementedError
