import unittest
import main
import simple_tg_bot


class Test(unittest.TestCase):
    def test_execution_time(self):
        try:
            if len(main.file_processing(open("numbers100k.txt"))) <= 100000:
                self.assertTrue(main.time_counter() < 0.5)

            elif 100000 < len(main.file_processing(open("numbers200k.txt"))) <= 200000:
                self.assertTrue(main.time_counter() < 1)

            elif 200000 < len(main.file_processing(open("numbers300k.txt"))) <= 300000:
                self.assertTrue(main.time_counter() < 2)

            elif 300000 < len(main.file_processing(open("numbers400k.txt"))) <= 400000:
                self.assertTrue(main.time_counter() < 3)

            elif 400000 < len(main.file_processing(open("numbers500k.txt"))) <= 500000:
                self.assertTrue(main.time_counter() < 4)

            elif 500000 < len(main.file_processing(open("numbers600k.txt"))) <= 600000:
                self.assertTrue(main.time_counter() < 5)

            elif 600000 < len(main.file_processing(open("numbers700k.txt"))) <= 700000:
                self.assertTrue(main.time_counter() < 6)

            elif 700000 < len(main.file_processing(open("numbers800k.txt"))) <= 800000:
                self.assertTrue(main.time_counter() < 8)
        except AssertionError as e:
            simple_tg_bot.send_message("Тест скорости провален")
            raise Exception(e)
        else:
            simple_tg_bot.send_message("Тест скорости пройден")


if __name__ == '__main__':
    unittest.main()