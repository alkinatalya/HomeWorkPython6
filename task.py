# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт
# сумму элементов списка, стоящих на нечётной позиции.
#Пример:
#- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
my_list= [0, 10, 5, 10, 3, 2]
print(my_list)
# Первое решение:
#sum = 0
#for i in range(1, len(my_list), 2):
#    sum += my_list[i]
#print(f"{sum}")
# Второе решение:
sum_positions = [el for i, el in enumerate(my_list, 1)if not i % 2]
print(f'{sum(sum_positions)}')

