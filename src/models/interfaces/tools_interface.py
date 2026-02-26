from abc import ABC, abstractmethod


class InterfaceTools(ABC):
    @abstractmethod
    def list_tools(self) -> list:
        ...

    @abstractmethod
    def get_tools_for_tags(self) -> list:
        ...

    @abstractmethod
    def create_tools(self) -> None:
        ...

    @abstractmethod
    def delete_tools(self) -> None:
        ...
