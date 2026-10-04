n = 5
i = 1
total_sum = 0
flag = False
while i <= n:
    print("Input result for test №", i)
    mark = int(input())

    if not(0 <= mark <= 100):
        print("Input error")
        # flag = True
        break

    total_sum += mark
    i += 1

# if flag == False:   # if not flag:
else:
    avg = total_sum / n 

    if avg < 60:
        print("F")
    elif avg <= 79:
        print("D")
    elif avg <= 89:
        print("C")
    elif avg <= 94:
        print("B")
    else:
        print("A")
