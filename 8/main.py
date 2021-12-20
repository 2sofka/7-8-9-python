"""
Загрузим тексты (книги) для работы из библиотеки nltk. 
"""
from nltk import book

"""
выведем список текстов (книг).
"""

print(book.text1)

"""
Поиск в текстах. Найдем тексты, в которых встречается слово «monstrous».
"""

print(book.text1.concordance("monstrous"))

"""
Определим, какие еще слова встречаются в одном контексте вместе со словом
monstrous с помощью функции similar. С помощью функции common_contexts
можно исследовать контексты, в которых встречаются оба эти слова.
"""

print(book.text1)
print(book.text2)
print("************************")
print(book.text1.similar("monstrous"))
print("************************")
print(book.text2.similar("monstrous"))
print("************************")
print(book.text2.common_contexts(["monstrous", "very"]))


book.text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])

"""
С помощью метода len можно узнать длину текста от начала до конца, включая
слова и пунктуацию.
"""

print(len(book.text3))

"""
Для того, чтобы получить все токены и затем отсортировать их используются
следующие команды:
"""

print(set(book.text3))
t3 = sorted(set(book.text3))
print(t3)

print(len(set(book.text3)))
print(len(book.text3) / len(set(book.text3)))

"""
Для подсчета, сколько раз слово встретилось в тексте, используется функция
count.
"""

print(book.text3.count("smote"))

"""
Подсчитайте для своего текста, с какой вероятностью это слово встретилось в
тексте.
"""


def lexical_diversity(text: str) -> float:
    return len(text) / len(set(text))


def percentage(count: int, total: int) -> float:
    return 100 * count / total


print(lexical_diversity(book.text3))

print(lexical_diversity(book.text5))

print(percentage(4, 5))

print(percentage(book.text4.count('a'), len(book.text4)))

"""
Во многих лингвистических моделях текст рассматривается как набор слов.
Рассмотрим, какие возможности предоставляет Python для этого.
"""

print(book.sent1)

print(len(book.sent1))

print(lexical_diversity(book.sent1))

"""
Мы можем соединить наборы слово с помощью оператора +:
"""

str1 = ["holly", "xmas", "bell", "tree"]
str2 = ["egg", "rabbit", "Easter", "chocolate"]

print(str1 + str2)
print(book.sent4 + book.sent1)

book.sent1.append("Some")

print(book.sent1)

"""
С помощью индекса мы можем обратиться к любому слову нашей
коллекции. Например:
"""

print(book.text4[173])

print(book.text4.index('awaken'))

"""
Мы можем также выделить диапазон из коллекции. Например:
"""

print(book.text5[16715:16735])

print(book.text6[1600:1625])

"""
Для того, чтобы отсортировать нашу коллекцию необходимо использовать
метод sorted(). Например:
"""

print(sorted(book.text6))

"""
Если вам необходимо список слов вновь склеить в единую строку, то для
этого используется команда join(). Например:
"""

s = ' '.join(['Monty', 'Python'])

print(s)
print(s.split())

"""
С помощью функции FreqDist() можно найти самые частотный слова для
документа. Например:
"""

fdist1 = book.FreqDist(book.text1)
print(fdist1)
vocabulary1 = fdist1.keys()
print(tuple(vocabulary1)[:50])
print(fdist1['whale'])

"""
Построим график для первых 50 самых частотных слов:
"""

fdist1.plot(50, cumulative=True)

"""
Если нас интересуют слова, длина которых больше 15 символов, то для этого
необходимо написать следующий код:
"""

V = set(book.text1)
long_words = [w for w in V if len(w) > 15]
sorted(long_words)

"""
Для того, чтобы найти коллокации мы вначале попробуем найти так называемые
биграммы с помощью функции bigrams():
"""

print(tuple(book.bigrams(['more', 'is', 'said', 'than', 'done'])))

"""
Однако, обычно хочется извлекать не просто биграммы, а именно коллокации –
частотные слова, которые в тексте обычно встречаются вместе. Для этого в Python удобно
использовать функцию collocations():
"""

print(book.text4.collocations())
