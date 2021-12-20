matrix = [['a', 'b', 'c', 'd', 'e'],
          ['f', 'g', 'h', 'i', 'j'],
          ['k', 'l', 'm', 'n', 'o'],
          ['p', 'q', 'r', 's', 't'],
          ['u', 'v', 'w', 'x', 'y'],
          ['x', '-', ',', ';', ' ']]


def polibii(bukva):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if bukva == matrix[i][j]:
                return i + 1, j + 1


def unpolibii(i, j):
    return matrix[i-1][j-1]


def main():
    print("Рончинский Андрей")
    text = input("Введите текст для шифрования: ")
    matrix = [[0, 0] for _ in range(len(text))]
    i = 0
    for bukva in text.lower().replace('j', 'i'):
        print(polibii(bukva))
        matrix[i] = polibii(bukva)
        i += 1
    print("Дешифр")

    for _ in range(len(matrix)):
        print(unpolibii(matrix[_][0], matrix[_][1]))


if __name__ == "__main__":
    main()
