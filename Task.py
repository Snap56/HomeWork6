# Задача: предложить улучшения кода для уже решённых задач:

# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension



list1 = [1.1, 1.2, 3.1, 5, 10.01]
list1 = list(map(lambda i: abs(i)%1,list1))
list1 = list(filter(lambda e:e!=0,list1))
print(round(max(list1),5) - round(min(list1),5))

