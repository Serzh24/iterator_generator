import hashlib

def get_list(path):
    with open(path, encoding='utf-8') as file:
        text = file.readlines()

    for string in text:
        hash = hashlib.md5(string.strip().encode('utf-8'))
        yield hash.hexdigest()


if __name__ == '__main__':
    for el in get_list('list.txt'):
        print(el)