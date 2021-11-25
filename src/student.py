from src.cpf import CPF
from src.email import Email
from src.phone import Phone


class Student:
    def __init__(self, cpf: CPF, email: Email, name: str) -> None:
        self.cpf = cpf
        self.email = email
        self.name = name
        self.phones = []

    def add_phone(self, phone: Phone) -> None:
        self.phones.append(phone)
