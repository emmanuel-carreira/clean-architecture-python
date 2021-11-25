import unittest

from school.domain.phone import Phone


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

    def test_phones_with_the_same_ddd_and_number_should_be_equal(self):
        phone_one = Phone('12', '12345-6789')
        phone_two = Phone('12', '12345-6789')
        self.assertEqual(phone_one, phone_two)

    def test_phones_without_the_same_ddd_and_number_should_not_be_equal(self):
        phone_one = Phone('12', '12345-6789')
        phone_two = Phone('99', '12345-6789')
        phone_three = Phone('12', '98765-4321')
        phone_four = Phone('99', '98765-4321')
        self.assertNotEqual(phone_one, phone_two)
        self.assertNotEqual(phone_one, phone_three)
        self.assertNotEqual(phone_one, phone_four)
