class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password
        
        
class User:
    """
    Класс пользователя, содержащий атрибуты: логин, пароль
    """
    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            self.password = password

if __name__ == '__main__':
    database = Database()
    while True:
        choise = int(input("Welcome!\nChoose an action\n1 - Login:\n2 - Sign up:\n"))
        if choise == 1:
            login = input("Введите логин: ")
            password = input("Введите пароль: ")
            password_confirm = input("Провтори: ")
            if login in database.data:
                if password == database.data[login]:
                    if password != password_confirm:
                        print("Пароли не совпадают, попробуйте ещё раз:")
                    else:

                        print(f'Вход произведен, {login} ')
                    continue
                else:
                    print("Неверный пароль")
            else:
                print("Пользователь не найден")
        if choise == 2:
            user = User(input("Введите логин: "), pw1 := input("Введите пароль: "), pw2 := input("Повторите пароль: "))
            if pw1 != pw2:
                print("Пароли не совпадают, попробуйте еще раз:")
                continue
            database.add_user(user.username,user.password)
        print(database.data)