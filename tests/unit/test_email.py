import unittest

from school.academic.domain.email import Email


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

    def test_emails_with_the_same_address_should_be_equal(self):
        email_one = Email("test@test.br")
        email_two = Email("test@test.br")
        self.assertEqual(email_one, email_two)

    def test_emails_with_different_addresses_should_not_be_equal(self):
        email_one = Email("test@test.br")
        email_two = Email("test_another_email@test.br")
        self.assertNotEqual(email_one, email_two)
