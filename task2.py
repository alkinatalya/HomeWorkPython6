#Напишите программу, которая возводит в квадрат каждый элемент списка
# и создает новый

nums = [5, 10, 6, 12]
# Первое решение
#ret = []
#def square(nums, ret):
#    for i in nums:
#        ret.append(i **2)
#    return ret
#n = square(nums, ret)
#print(ret)
# Второе решение
ret=[i*i for i in nums]
print(ret)