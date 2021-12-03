from school.domain.cpf import CPF
from school.domain.email import Email
from school.domain.phone import Phone
from school.domain.max_phones_allowed import MaxPhonesAllowed


class Student:
    def __init__(self, cpf: CPF, email: Email, name: str) -> None:
        self.cpf = cpf
        self.email = email
        self.name = name
        self.phones = []

    def add_phone(self, phone: Phone) -> None:
        if len(self.phones) == 2:
            raise MaxPhonesAllowed("Maximum numbers of phones already registered!")
        self.phones.append(phone)
