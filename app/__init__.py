from .validators import check_password
from .db_handlers import get_users_from_db, search_user


def site():
    login = input('Логин: ')
    password = input('Пароль: ')
    found_user_db: list[str] = []
    users_list = get_users_from_db()
    check_user = search_user(users_list, login)
    if not check_user:
        print('Пользователь не найден')
        site()
    db_login, db_password = found_user_db
    if not check_password(password, db_password):
        print('Неправильный пароль!')
        site()
    print('Вы успешно вошли в систему!\nПриветствую', login)
