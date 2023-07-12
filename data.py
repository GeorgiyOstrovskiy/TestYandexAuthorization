logins = ['login', 'login@yandex.ru']
login_and_password = {'login': 'password', 'login@yandex.ru': 'password'}
incorrect_password = 'qwertyt23'
code = '123456'
phone = '+79999999999'
defunct_login = 'rtghbndfgt3'


def get_password_for_login(login):
    password = login_and_password[login]
    return password


error_authorization_defunct_login = 'Нет такого аккаунта. Проверьте логин или войдите по телефону'
error_unsuccessful_authorization_login = 'Неверный пароль'
error_unsuccessful_authorization_phone = 'Неправильный код, попробуйте ещё раз'

link = 'https://passport.yandex.ru/auth/add?origin=dzen&retpath=https%3A%2F%2Fsso.passport.yandex.ru%2Fpush%3Fuuid%' \
       '3D41c22b8e-1071-4ae0-91c6-de18105b355d%26retpath%3Dhttps%253A%252F%252Fdzen.ru%252F%253Fask_permissions%253' \
       'D1&backpath=https%3A%2F%2Fdzen.ru%2F-chunked%2F%3Fyredirect%3Dtrue%26utm_referer%3Dwww.google.com'
