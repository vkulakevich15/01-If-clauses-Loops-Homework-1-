total = float(input("Input total amount of your orders "))
current_sum = float(input("Input total price for current order "))

if total < 0 or current_sum < 0:
    print("Input error")
else:
    discount = 0

    if total >= 5000:
        discount = 15
    elif total >= 1000:
        discount = 10
    elif total >= 500:
        discount = 5

    if current_sum > 1000:
        discount += 10
    elif current_sum > 300:
        discount += 5

    if discount > 25:
        discount = 25

    current_pay = current_sum * (100 - discount) / 100

    print("Discount: ", str(discount) + "%")
    print("Sum today for pay: ", current_pay)