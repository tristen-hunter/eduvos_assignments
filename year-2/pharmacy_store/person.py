from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name: str, surname: str, cell_num: str, email: str) -> None:
        self.name = name
        self.surname = surname
        self.cell_num = cell_num
        self.email = email

    @abstractmethod
    def insert_person(self, conn) -> None:
        pass

    @abstractmethod
    def delete_person(self, conn) -> None:
        pass

    @classmethod
    @abstractmethod
    def display_all(cls, conn) -> None:
        pass
