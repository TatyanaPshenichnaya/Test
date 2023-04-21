# получение данных от пользователя с проверкой их корректности
try:
    # Получение последовательности чесел и преобразование её в список
    a = [int(i) for i in input('Введите последовательность чисел через пробел:').split()]
    b = int(input('Введите любое число:'))
except  ValueError:
    print('Некорректый ввод!')

# функция сортировки списка по возрастанию элементов
import random


def fast_sort(array):
    if len(array) < 2:  # базовый случай рекурсии: массивы длиной 0 и 1 уже отсортированы
        return array
    else:  # рекурсивный случай
        p_ind = random.choice(range(len(array)))  # индекс случайного элемента
        p = array[p_ind]  # случайный элемент
        left = [i for i in (array[:p_ind] + array[p_ind + 1:]) if i <= p]  # массив элементов, меньших случайного p
        right = [i for i in (array[:p_ind] + array[p_ind + 1:]) if i > p]  # массив элементов, больших случайного p
        return fast_sort(left) + [p] + fast_sort(right)


# отсортируем массив
a = fast_sort(a)
print(a)


# функция, проверяющая вхождение в отсортированный массив числа
def is_number_in_array(array, number):
    return array[0] <= number <= array[-1]


# функция определения позиции элемента через алгоритм двоичного поиска
# Устанавливается номер позиции элемента, который меньше введенного пользователем
# числа, а следующий за ним больше или равен этому числу.
def binary_search(array, element, left, right):
    middle = (right + left) // 2  # находимо середину

    if left >= right:  # если левая граница превысила правую,
        return middle  # возвращаем индекс предыдущего элемента

    if array[middle] == element and array[middle - 1] < element:  # если элемент в середине,
        return middle - 1  # возвращаем индекс предыдущего элемента
    elif array[middle] < element:  # если элемент меньше элемента в середине
        # рекурсивно ищем в правой половине
        return binary_search(array, element, middle + 1, right)
    else:  # иначе в левой
        return binary_search(array, element, left, middle - 1)


c = 0 # начальная граница массива
d = len(a) - 1 # конечная граница массива
if is_number_in_array(a, b):
    print("Индекс позиции элемента:", binary_search(a, b, c, d))
else:
    print("Введенный элемент за пределами массива")