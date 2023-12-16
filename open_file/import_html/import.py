# # get answer a user, and set to index.html

# # <h1>Джулия Тейлор</h1><p>Моя специализация - информатика, я являюсь членом джаз-клуба и надеюсь стать разработчиком мобильных приложений после того, как получу высшее образование.</p>

import os

def main():
    h1 = '<h1>'
    p = '<p>'
    name_user = input('Enter your name: ')
    about_user = input('Tell us about yourself: ')
    in_file = open('index.html', 'r')
    temp_file = open('temp.html', 'w')
    for line in in_file:
        if line != 




    
