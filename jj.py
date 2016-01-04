# -*- coding: utf-8 -*-
# функція меню
def menu(list, question):
    for entry in list:
        print 1 + list.index(entry),
        print ") " + entry
 
    try:
        return input(question) - 1
    except NameError:
        print 'Будь-ласка, введіть число від 1 до 8'
 
# визначаэмо наш список опцій для меню
options = ['A','B','C','D','E','F','H','I']
 
# викликаємо нашу функцію
answer = menu(options, 'Яка ваша улюблена літера? ')
 
try:
    print 'Ваша відповідь ' + (options[answer])
except:
    print 'Неправильна відповідь. Спробуйте ще раз.'
