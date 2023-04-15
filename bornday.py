date=input('Введите дату рождения Пушкина А.С.: ')
if date == '1799':
    day=input('А какой день и месяц?')
    if day == '26.5'or day == '26.05'or day == '26/5'or day == '26/05'or day == '26 мая':
        print('Верно!')
    else:
        print('Неверно!')
else:
    print('Неверно!')