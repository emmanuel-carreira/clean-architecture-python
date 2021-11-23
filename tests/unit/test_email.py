import unittest

from src.email import Email


class EmailTest(unittest.TestCase):
    def test_should_not_create_email_with_none_address(self):
        with self.assertRaises(ValueError):
            Email(None)

    def test_should_not_create_email_with_empty_address(self):
        with self.assertRaises(ValueError):
            Email("")

    def test_should_not_create_email_with_invalid_address(self):
        with self.assertRaises(ValueError):
            Email("test@test")

    def test_should_create_email_with_valid_address(self):
        email = Email("test@test.br")
        self.assertEqual(email.address, "test@test.br")
