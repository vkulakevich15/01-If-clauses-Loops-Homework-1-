while True:
    n = int(input("Input number of mushrooms"))

    if n < 0:
        print("Input error")
    else:
        last_digit = n % 10
        two_last_digits = n % 100

        if last_digit == 1:
            if two_last_digits == 11:
                print("Мы собрали", n, "грибов")
            else:
                print("Мы собрали", n, "гриб")

        elif 2 <= last_digit <= 4:
            if 12 <= two_last_digits <= 14:
                print("Мы собрали", n, "грибов")
            else:
                print("Мы собрали", n, "гриба")
                
        else:
            print("Мы собрали", n, "грибов")