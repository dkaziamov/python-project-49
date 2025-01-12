def make_user(name: str, age: int) -> dict:
    return {"name": name, "age": age}


def format_user(dictionary: dict) -> str:
    return f"{dictionary['name']}, {dictionary['age']}"


dictionary = make_user('Bob', 42)
print(format_user(dictionary))
