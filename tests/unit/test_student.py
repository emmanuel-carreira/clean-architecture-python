import unittest

from school.academic.domain.phone import Phone
from school.academic.domain.student.student_builder import StudentBuilder
from school.academic.domain.max_phones_allowed import MaxPhonesAllowed


class StudentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.student_builder = StudentBuilder()

    def test_do_not_allow_to_register_more_than_two_phones(self):
        student = self.student_builder.with_cpf_email_and_name(
            '111.111.111-11', 'test@test.com', 'Irrelevant name'
        ).with_phone('99', '99999-9999').with_phone('88', '88888-8888').create()
        third_phone = Phone('77', '77777-7777')
        with self.assertRaises(MaxPhonesAllowed):
            student.add_phone(third_phone)
