a = int(input("введите размер выручки "))
b = int(input("введите размер издержек "))
if a > b:
    print("Вы работаете с прибылью ")
    r = (a - b) / a # рентабельность
    print("Рентабельность " , r)
    c = a - b   # прибыль
    y = int(input("введите количество сотрудников в вашей фирме "))
    p = c / y # прибыль на сотрудника
    print(p)
else:
    print("Вы в убытке")



