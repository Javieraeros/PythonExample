import json
from random import randint


def read_users(users: int = 3) -> list:
    file = open("users.json", "r+")
    json_list: list = json.loads(file.read())
    file.close()
    if users > len(json_list):
        users = len(json_list)
    random = []
    result = []
    for i in range(users):
        next_random = randint(0, len(json_list) - 1)
        while next_random in random:
            next_random = randint(0, len(json_list) - 1)

        random.append(next_random)
    for i in random:
        result.append(json_list[i])

    return result


def main():
    print(json.dumps(read_users(2), ensure_ascii=False, indent=4))


if __name__ == "__main__":
    main()
