import unittest

from src.cpf import CPF


class CPFTest(unittest.TestCase):
    def test_should_not_create_cpf_with_none_number(self):
        with self.assertRaises(ValueError):
            CPF(None)

    def test_should_not_create_cpf_with_empty_number(self):
        with self.assertRaises(ValueError):
            CPF("")

    def test_should_not_create_cpf_with_invalid_number(self):
        with self.assertRaises(ValueError):
            CPF("123.456.789/0001-01")

    def test_should_create_cpf_with_valid_number(self):
        cpf = CPF("123.456.789-00")
        self.assertEqual(cpf.number, "123.456.789-00")
