fam_people = {0:'Пушкин А.С.', 1:'Суворов А.В.', 2:'Петр I', 3:'Иван Грозный', 4:'Екатерина Великая'}
years = {0:'1799', 1:'1730', 2:'1672', 3:'1530', 4:'1729'}
isplaying=True
while isplaying:
    year, cont = '', ''
    corr, err, i = 0, 0, 0
    while i in fam_people:
        year = input(f'Введите год рождения известной личности: {fam_people[i]} :')
        if year == years[i]:
            corr+=1
        else:
            err+=1
        i+=1
    res = int(corr*100/i)
    print('Кол-во правильных ответов: ', corr)
    print('Кол-во ошибок: ', err)
    print(f'Ваш результат составил {res} %')
    while cont != 'да' and cont !='нет':
        cont = input('Хотите повторить? (да/нет): ')
        if cont=='нет':
            isplaying=False
print('Bye!')
