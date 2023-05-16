def check_password(raw_password: str, hash_password: str) -> bool:
    hashed_password = raw_password  # some hash function
    return hashed_password == hash_password


if __name__ == '__main__':
    print(__name__)
