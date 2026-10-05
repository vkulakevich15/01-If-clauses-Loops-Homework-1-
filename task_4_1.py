nom1 = 1    # a
nom2 = 2    # b
nom3 = 5    # c

# total = 100
total = int(input("Input total sum of money "))


# 1 * 10 + 2 * 0 + 5 * 0
# 1 * 8    2 * 1   5 * 0
# 1 * 6    2 * 2   5 * 0   
# 1 * 4    2 * 3   5 * 0
# 1 * 2    2 * 4   5 * 0
# 1 * 0 +  2 * 5 + 5 * 0

# 1 * 5   2 * 0   5 * 1
# 1 * 3   2 * 1 + 5 * 1
# 1 * 1   2 * 2   5 * 1

# 1 * 0 + 2 * 0 + 5 * 2

c = 0
while c <= total // nom3:  # 10 // 5
    b = 0
    while b <= (total - c * nom3) // nom2:  # (10 - 5 * c) // 2
        # 10 - 5 * 1 - 2 * 1 = 3 // 1
        a = (total - c * nom3 - b * nom2) // nom1
        if c * nom3 + b * nom2 + a * nom1 == total:
            print(a, b, c)
        b += 1
    c += 1