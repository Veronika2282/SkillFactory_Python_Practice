per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

money = float(input('Введите сумму вклада без пробелов и запятых: '))
# здесь нужна проверка ввода, т.к. при некорректном вводе программа не может дальше работать
# после некорректного ввода должно выводиться сообщение об ошибке и повторно запускаться ввод с клавиатуры
# но мы пока этого не умеем ¯\_(ツ)_/¯

tkb = int(money * per_cent['ТКБ'] / 100)
skb = int(money * per_cent['СКБ'] / 100)
vtb = int(money * per_cent['ВТБ'] / 100)
sber = int(money * per_cent['СБЕР'] / 100)
# int добавлено в целях соответствия типа объектов в списке указанному в задании: deposit = [5600, 5900, 4280, 4000].
# Присвоить численные значения переменным можно было и так: tkb = money * per_cent['ТКБ'] / 100.
# Тогда в нашем случае они бы записались в виде float: deposit = [5600.0, 5900.0, 4280.0, 4000.0].

deposit = [tkb, skb, vtb, sber]

print("Максимальная сумма, которую вы можете заработать —", max(deposit))
