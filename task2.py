# Скидка по накоплениям и сумме текущей покупки
# общая сумма накопленных покупок (число ≥ 0)
# сумма текущей покупки (число ≥ 0)
# На основе накоплений определяется базовый уровень скидки:

# если накопления < 500 → скидка 0% , т.е. < 500 -> 0
# если 500–999 → скидка 5%          , т.е. < 1000 -> 5%
# если 1000–4999 → скидка 10%       , т.е. < 5000 -> 10%
# если ≥ 5000 → скидка 15%          , т.е. >= 5000 -> 15%

# Дополнительная скидка:
# если текущая покупка > 300 → добавить ещё 5%
# если текущая покупка > 1000 → добавить 10% (вместо 5%)
# максимальная итоговая скидка — 25%
# Если введены отрицательные числа — вывести "Input error".

# Программа должна вывести:

# итоговую скидку
# сумму к оплате после применения скидки
# Пример
# Ввод:
# Накопления: 1200
# Текущая покупка: 450

# Вывод:
# Итоговая скидка: 15%
# К оплате: 382.5

savings = float(input("Input the amount of savings"))    # накопления
current_purchase = float(input("Input the amount of current_purchases "))   # текущая покупка

if savings < 0 or current_purchase < 0:
    print("Input error")
else:
    discount = 0

    if savings < 500:
        discount = 0
    elif savings < 1000:
        discount = 5
    elif savings < 5000:
        discount = 10
    else:
        discount = 15

    if current_purchase > 1000:
        discount = discount + 10
    elif current_purchase > 300:
        discount = discount + 5
    if discount > 25:
        discount = 25

    discount_sum = current_purchase * discount / 100
    total_sum = current_purchase - discount_sum   

    print("Итоговая скидка:", discount, "%")
    print("К оплате:", total_sum)
