# Итоговая буквенная оценка
# юзик вводит 5 целых чисел — результаты пяти тестов (каждое от 0 до 100). Если хотя бы одно значение вне диапазона 0–100, программа выводит "Input error" и завершает работу.
# Если все оценки корректны:
# вычислить среднее арифметическое пяти чисел
# определить итоговую буквенную оценку по шкале:
# < 60 → F
# 60–79 → D
# 80–89 → C
# 90–94 → B
# 95–100 → A
# Вывести только итоговую буквенную оценку

A = int(input("Input number"))
B = int(input("Input number"))
C = int(input("Input number"))
D = int(input("Input number"))
F = int(input("Input number"))

if A < 0 or A > 100:
    print("Input error")
elif B < 0 or B > 100:
    print("Input error")
elif C < 0 or C > 100:
    print("Input error")
elif D < 0 or D > 100:
    print("Input error")
elif F < 0 or F > 100:
    print("Input error")
else:
    average = (A + B + C + D + F) / 5

    if average < 60:
        print("F")
    elif average < 80:
        print("D")
    elif average < 90:
        print("C")
    elif average < 95:
        print("B")
    else:
        print("A")