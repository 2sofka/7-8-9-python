text = input("Введите текст для шифрования:")
n = len(text)

key = 'andreyrochisk'
print(key)
m = len(key)

d = n // m
e = n % m
x = ''
for i in range(e):
    x += key[i]

vighner = ""
c = d * key + x
for i in range(n):
    vighner += chr(ord(text[i]) + ord(c[i]))

print("Шифр: " + vighner)
#процесс декодировки
devighner = ""
n = len(vighner)

for i in range(n):
    devighner += chr(ord(vighner[i]) - ord(c[i]))

print("Дешифр: " + devighner)
