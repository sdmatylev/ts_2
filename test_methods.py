import unittest
import main
from random import randint
import functools
import simple_tg_bot

numbers = []
for i in range(100000):
    numbers.append(randint(1, 2))


class Test(unittest.TestCase):
    is_test_right = 1

    def test_min(self):
        try:
            self.assertEqual(main._min(numbers), min(numbers))

        except AssertionError as e:
            Test.is_test_right = 0
            simple_tg_bot.send_message("Тест минимума провален")
            raise Exception(e)

    def test_max(self):
        try:
            self.assertEqual(main._max(numbers), max(numbers))

        except AssertionError as e:
            Test.is_test_right = 0
            simple_tg_bot.send_message("Тест максимума провален")
            raise Exception(e)

    def test_sum(self):
        try:
            self.assertEqual(main._sum(numbers), sum(numbers))

        except AssertionError as e:
            Test.is_test_right = 0
            simple_tg_bot.send_message("Тест суммы провален")
            raise Exception(e)

    def test_mult(self):
        try:
            self.assertEqual(main._mult(numbers), functools.reduce(lambda x, y: x * y, numbers))

        except AssertionError as e:
            Test.is_test_right = 0
            simple_tg_bot.send_message("Тест произведения провален")
            raise Exception(e)

    def test_check_file(self):
        try:
            self.assertTrue(main.file != 0)

        except AssertionError as e:
            Test.is_test_right = 0
            simple_tg_bot.send_message("Файл не найден")
            raise Exception(e)

    def test_results(self):
        if Test.is_test_right:
            simple_tg_bot.send_message("Тесты методов пройдены")


if __name__ == "__main__":
    unittest.main()