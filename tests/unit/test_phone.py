import unittest

from src.phone import Phone


class PhoneTest(unittest.TestCase):
    def setUp(self) -> None:
        self.valid_ddd = "99"
        self.valid_number = "99999-9999"

    def test_should_not_create_phone_with_none_ddd(self):
        with self.assertRaises(ValueError):
            Phone(None, self.valid_number)

    def test_should_not_create_phone_with_empty_ddd(self):
        with self.assertRaises(ValueError):
            Phone("", self.valid_number)

    def test_should_not_create_phone_with_invalid_ddd(self):
        with self.assertRaises(ValueError):
            Phone("(99)", self.valid_number)

    def test_should_not_create_phone_with_none_number(self):
        with self.assertRaises(ValueError):
            Phone(self.valid_ddd, None)

    def test_should_not_create_phone_with_empty_number(self):
        with self.assertRaises(ValueError):
            Phone(self.valid_ddd, "")

    def test_should_not_create_phone_with_invalid_number(self):
        with self.assertRaises(ValueError):
            Phone(self.valid_ddd, "99999999")

    def test_should_create_phone_with_valid_ddd_and_number(self):
        phone = Phone(self.valid_ddd, self.valid_number)
        self.assertEqual(phone.ddd, self.valid_ddd)
        self.assertEqual(phone.number, self.valid_number)
