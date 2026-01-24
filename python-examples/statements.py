s1 = input("Введите имя поьзователя: ")
age = input("Введите возраст поьзователя: ")
height = int(input("Введите рост поьзователя: "))
weight = int(input("Введите вес поьзователя: "))

isTrue = False

relation = height//weight


if relation == 2:
    isTrue = True


if isTrue:
    print("Raltion of height and weight really good! My congratulation")
else:
    print("That's not bad tho not perfect")
