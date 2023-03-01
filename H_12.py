per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}


def depost_calc(diction, money):

    deposit = list( map( lambda x: round(x / 100 * money ), diction.values()))

    max_deposit = max(deposit)
    text = "Максимальная сумма, которую вы можете заработать — " + str(max_deposit)
    return deposit, text

print(depost_calc(per_cent, int(input("Введите сумму вклада:"))))