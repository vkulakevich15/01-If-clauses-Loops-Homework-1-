# если собрали 1, 21, 31 ... - гриб == 1 на конце
# если собрали 2, 3, 4, 22, 23, 24 ... - гриба (2,3,4 == -а)
# если собрали 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 25, 30 ... - грибов
# используем % для опеределения окончания
# для диапазона - range(11, 15) (не включает 15!!!)




number = int(input("Input number of mushrooms"))

if number < 0:
    print("Input error")
elif number in range(11, 15):
    print("Мы собрали", number, "грибов")
elif number % 10 == 1:
    print("Мы собрали", number, "гриб")
elif number % 10 == 2 or number % 10 == 3 or number % 10 == 4:
    print("Мы собрали", number, "гриба")
else:
    print("Мы собрали", number, "грибов")