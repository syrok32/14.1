from abc import ABC, abstractmethod


class BaseProduct(ABC):
    @abstractmethod
    def get_name(self):
        pass
