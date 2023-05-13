def get_users_from_db():
    return [
        ['login', 'password'],
        ['admin@gmail.com', 'admin'],
    ]


def search_user(users_list: list[list[str]], input_login: str) -> list:
    found_user_db = []
    for user in users_list:
        user_login, user_password = user
        if input_login == user_login:
            found_user_db = user
            break
    return found_user_db
