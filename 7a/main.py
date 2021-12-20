def encypt_func(txt, s):
    result = ""
    for i in range(len(txt)):
        char = txt[i]
        result += chr(ord(char) + s)
    return result


def unencypt_func(txt, s):
    result = ""
    for i in range(len(txt)):
        char = txt[i]
        result += chr(ord(char) - s)
    return result


def main():
    # check the above function
    txt = input("Введите фразу для шифрования: ")
    s = 15
    encypt = encypt_func(txt, s)
    unencypt = unencypt_func(encypt, s)
    print("Фраза для шифрования : " + txt)
    print("Ключ: " + str(s))
    print("Шифр: " + encypt)
    print("Дешифр: " + unencypt)


if __name__ == "__main__":
    main()
