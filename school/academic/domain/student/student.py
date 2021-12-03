from school.academic.domain.email import Email
from school.academic.domain.phone import Phone
from school.academic.domain.max_phones_allowed import MaxPhonesAllowed
from school.shared.domain.cpf import CPF


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
