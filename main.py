import time
from random import randint


def get_generated_file(file_name, symbol_count):
    file = open(file_name, "w")
    for i in range(symbol_count):
        file.write(str(randint(1, 2)) + " ")
    file.close()
    file = open(file_name, "r")
    return file


def file_processing(file):
    all_numbers = []
    for number in file.readline().split():
        all_numbers.append(int(number))
    file.close()
    return all_numbers


def _min(numbers):
    my_min = 999999999999999
    for number in numbers:
        if number < my_min:
            my_min = number
    return my_min


def _max(numbers):
    my_max = -999999999999999
    for number in numbers:
        if number > my_max:
            my_max = number
    return my_max


def _sum(numbers):
    my_sum = 0
    for number in numbers:
        my_sum += number
    return my_sum


def _mult(numbers):
    mult = 1
    for number in numbers:
        mult *= number
    return mult


def time_counter():
    return end_time - start_time


file_name = "numbers.txt"
symbol_count = 900000
file = get_generated_file(file_name, symbol_count)
numbers = file_processing(file)

start_time = time.time()

print("Минимальное число из файла:", _min(numbers))
print("Максимальное число из файла:", _max(numbers))
print("Сумма чисел из файла:", _sum(numbers))
print("Произведение чисел из файла:", _mult(numbers))

end_time = time.time()
print("Время работы программы:", time_counter())