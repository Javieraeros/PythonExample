def ask_ok(prompt, retries=4, reminder='Please try again'):
    for i in range(retries):
        print(prompt)
        ok = input()
        if ok in ('y', 'yes'):
            return True
        elif ok in ('n', 'nos'):
            return False
        else:
            print(reminder)
    else:
        raise ValueError('Invalid User Response')


if __name__ == '__main__':
    ask_ok("Inténtalo")
