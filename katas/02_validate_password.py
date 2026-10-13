def is_valid_password(pwd):
    return (8 <= len(pwd) <= 20
            and any(c.isupper() for c in pwd)
            and any(c.isdigit() for c in pwd))
