a = "да"
a_1 = "Да"

v = 2020
n = input("Меня зовут Ксения. А тебя? ")
print("Привет, ",
      n, "!",
      sep="")
b = input("Поболтаем? ")

if b == a or b == a_1:
    print("Что-то перехотелось, извини.")

else:
    print("Хорошо. Помолчим...")
    age = int(input("А сколько тебе лет, " + n + "?"))
    print("Год рождения ", v - age, ". Хм... Помолчим!", sep="")
    print('старость не радость')
