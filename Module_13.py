ticket_price = {'under 18': 0, '18 to 24': 990, '25 and older': 1390}
all_tickets_price_list = []
participants = int
age = int
n = 1
while participants:
    try:
        participants = int(input('Введите количество участников, которых вы хотите зарегистрировать: '))
    except ValueError as e:
        print("Вы ввели неверное значение. Попробуйте еще раз.")
        continue
    if participants is int:
        break
    else:
        while n <= participants:
            try:
                age = int(input('Введите возраст участника № %d: ' % n))
            except ValueError as e:
                print("Вы ввели неверное значение. Попробуйте еще раз.")
                continue
            if age is int:
                break
            else:
                n += 1
                if age < 18:
                    all_tickets_price_list.append(ticket_price['under 18'])
                elif age in range(18, 25):
                    all_tickets_price_list.append(ticket_price['18 to 24'])
                else:
                    all_tickets_price_list.append(ticket_price['25 and older'])
    if participants != 0:
        break

if participants > 3:
    print('Сумма к оплате с учетом скидки:', int(sum(all_tickets_price_list) * 0.9), 'рублей')
else:
    print('Сумма к оплате:', sum(all_tickets_price_list), 'рублей')
