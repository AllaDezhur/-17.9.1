array = list(map(int, input("Введите данные:  ").split()))
import random
def quick_sort(array): # использую метод быстрой сортировки
    if len(array) > 1:
        x = array[random.randint(0, len(array)-1)]  # случайное пороговое значение (для разделения на малые и большие)
        low = [i for i in array if i < x]
        eq = [i for i in array if i == x]
        high = [i for i in array if i > x]
        array = quick_sort(low) + eq + quick_sort(high)
    return array
array = quick_sort(array)
print(array)
#Использую бинарный поиск
element = int(input("Введите элемент: "))
start = 0
stop = len(array)
def binary_search(array, element, start, stop):
    if start > stop or element > array[stop-1]:
        return False
    middle = (start + stop) // 2
    if array[middle] == element:
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, start, middle - 1)
    else:  # рекурсивно ищем в правой половине
        return binary_search(array, element, middle + 1, stop)
index = binary_search(array, element, start, stop)
print(index)

if index is False:
     print("Этого числа нет в списке")
else:
 if index == 0:
  print(" Это первое число списка, следующее число имеет индекс = ",(index +1))
 elif index == stop - 1:
  print(" Это последнее число списка, предыдущее число имеет индекс = ",(index -1))
 else:
  print("Предыдущее число имеет индекс = ",(index-1)," следующее число имеет индекс =", (index + 1))
