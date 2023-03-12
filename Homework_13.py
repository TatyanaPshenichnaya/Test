def purchase_calc(n, age_list):
    total = 0
    for i in age_list:
        if 18 <= i < 25:
            total += 990
        elif i >= 25:
            total += 1390

    if len(age_list) > 3:
        total = total * 0.9

    return total

n = int(input("Введите количество билетов: "))
print("Сумма к оплате:", purchase_calc(n, age_list = [ int(input("Введите возраст участника: ")) for i in range(n)]) )