# Напишите программу, которая на вход получает
# два списка. Из первого списка, извлекаются 
# нечетные числа, из второго четные. Новый
# элемент добавляем в новый список и выводим
# результат.
list1 = [10, 20, 30, 45, 75] 
list2 = [35, 65, 40, 50, 60]

# Первый способ решения:
#list3 = []
#for i in list1:
#    if i %2 !=0:
#        list3.append(i)
#for j in list2:
#    if j %2 ==0:
#        list3.append(j)  
#print(list3)
# Второй способ решения:       
list4 =list(filter(lambda i: i % 2, list1))
list5 =list(filter(lambda i: not i %2, list2))
print(list4 +list5)