#задание 4
a = int(input())
q = int(input())
if a > q:
    s = a - q
    print(s)
elif a < q:
    s = a + q 
    print(s)
else:
    s = a 
    print (s)
#задание 5
a = str(input("Из какой вы страны?"))
if a == "Италия":
    print("Ваша национальная еда - пицца!")
elif a == "Россия":
    print("Ваша национальная еда - борщ!")
elif a == "Корея":
    print("Ваша национальная еда - рамен и кимчи!")
elif a == "Грузия":
    print("Ваша национальная еда - хинкали!")
else:
    print("Такой страны в базе нет, но у вас тоже вкусная еда!")


    