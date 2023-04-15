date, day = '', ''
days = ['26.5','26.05','26/5','26/05','26 мая']
while date != '1799':
    date=input('Введите дату рождения Пушкина А.С.: ')

while day not in days:
    day=input('Введите день и месяц рождения Пушкина А.С.: ')
    if day in days:
        print('Верно!')