# 1. Функция Конвертации Валют - Написать  чистую  функцию  для  конвертации  валюты,
# которая  не  изменяет исходные данные.
import random
from functools import reduce


def change_money(amount):
    return amount * 0.00025


# print(change_money(450))

# 2. Генератор Функций - Создать функцию высшего порядка,
#    которая возвращает другую функцию для возведения числа в указанную степень.
def wrapper(power):
    return lambda x: x ** power


numbers = [1, 2, 3, 4, 5]
print(list(map(wrapper(3), numbers)))


# 3. Безопасный Список-Реализовать функцию, которая копирует список перед выполнением операций,
#    чтобы оригинальный список оставался неизменным.
def copy(my_list):
    return [x for x in my_list]


# 4. Функция Суммирования-Написать чистую функцию для суммирования всех элементов в кортеже.
def sum(my_tuple):
    return reduce(lambda x, y: x + y, my_tuple)


nums = (1, 2, 3)


# print(sum(nums))


# 5. Функция Композиции - Создать  функцию  высшего  порядка,  которая  принимает  две  функции и возвращает их
# композицию.
def compose(f, g):
    return lambda x: f(g(x))


def add(x):
    return x + 2


def power_of_two(x):
    return x ** 2


def solve5():
    caller = compose(power_of_two, add)
    print(caller(5))


solve5()


# compose(f=lambda x, y: x + y, g=lambda x: x > 10)

# 6. Функция Фильтрации - Реализовать чистую функцию для фильтрации списка чисел, возвращающую новый список без
# изменения исходного.
def task6(numbers):
    return list(filter(lambda x: x % 2 == 0, numbers))


# print(task6(numbers))
# print(numbers)


# 7. Калькулятор Налогов - Написать функцию, которая рассчитывает налоги на основе дохода, не изменяя исходные данные.
def task7(amounts):
    return list(map(lambda x: x * 0.12, amounts))


amounts = [1000, 2000, 3000, 4000, 5000]
print(task7(amounts))
print(amounts)


# 8. Функция Обратного Вызова - Создать функцию высшего порядка, которая принимает
#    функцию обратного вызова и применяет её к элементам списка.
def callback_hello(name):
    print("Hello " + name)


def callback_goodbye(name):
    print("Goodbye " + name)


def task8(f):
    names = ['Adam', 'Bob', 'Charlie']
    for name in names:
        f(name)


def solve8():
    task8(callback_hello)
    task8(callback_goodbye)


solve8()


# 9. Генератор Случайных Чисел - Написать чистую функцию, которая генерирует список случайных чисел, не изменяя
# глобальное состояние.
def task9():
    return [random.randint(1, 100) for i in range(10)]


def solve9():
    print(task9())


# 10. Функция Мемоизации - Реализовать функцию мемоизации для ускорения вычисления рекурсивных функций.
def memoize(f):
    cache = {}

    def decorate(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]

    return decorate


@memoize
def fib(n):
    if n < 2:
        return n
    return fib(n - 2) + fib(n - 1)



def solve10():
    print('fib(20) =', fib(20))
    print(fib(20))


# 11. Функция Разделения Строки-Создать  чистую  функцию,  которая  принимает  строку  и  возвращает  список слов,
# не изменяя исходную строку.
def task11(line):
    return line.split(" ")


def solve11():
    line = "Hello World!"
    print(task11(line))
    print(line)


solve11()


# 12. Функция Поиска Минимума и Максимума - Написать функцию, которая находит минимальное и максимальное число в
# неизменяемом кортеже.
def task12():
    pass


def solve12():
    pass


# 14. Функция Сортировки - Создать чистую функцию для сортировки копии списка, оставляя исходный список без изменений.
def task14(my_list):
    return sorted(my_list)


my_list = [1, 2, 6, 4, 3, 5, 7, 8, 9]
print(task14(my_list))
print(my_list)

# 15. Генератор Предикатных Функций - Написать функцию высшего порядка,
#     которая создает и возвращает функцию - предикат на основе заданного условия.

my_tuple = (1, 2, 3)
print(max(my_tuple), min(my_tuple))


# def generate_even_odd_predicates():
#     yield lambda x: x % 2 == 0
#     yield lambda x: x % 2 != 0
#
#
# even_odd_predicator = generate_even_odd_predicates()
#
# for i in range(1, 6):
#     even_predicate = next(even_odd_predicator)
#     odd_predicate = next(even_odd_predicator)


def freeze_dict(input_dict):
    """Принимает   словарь   и   возвращает   неизменяемое   представление   его содержимого."""
    # Создание списка пар ключ-значение
    items = input_dict.items()
    # Преобразование списка в frozenset для обеспечения неизменяемости
    frozen_dict = frozenset(items)
    return frozen_dict


# Примериспользованияфункции
original_dict = {"apple": "green", "banana": "yellow"}
frozen_dictionary = freeze_dict(original_dict)
print(frozen_dictionary)

