class QuantitativeSpeechAssessments:
    PUNCTUATION_MARKS = ('.', ',', ':', ';', '?', '!', '...', '-', '"', "'", '(', ')')
    PREPOSITIONS = (
        'без', 'безо', 'близ', 'в', 'во', 'вместо', 'вне', 'для', 'до', 'за', 'из', 'изо', 'из-за', 'из-под', 'к', 'ко',
        'кроме', 'между', 'меж', 'на', 'над', 'о', 'об', 'обо', 'от', 'ото', 'перед', 'передо', 'пред', 'пред', 'пo',
        'под',
        'подо', 'при', 'про', 'ради', 'с', 'со', 'сквозь', 'среди', 'у', 'через'
    )
    UNIONS = (
        'а', 'аж', 'благо', 'будто', 'вроде', 'да', 'дабы', 'даже', 'едва', 'ежели', 'если', 'же', 'затем', 'зато', 'и',
        'ибо', 'или', 'итак', 'кабы', 'как', 'когда', 'коли', 'коль', 'ли', 'либо', 'лишь', 'нежели', 'но', 'пока',
        'покамест', 'покуда', 'поскольку', 'притом', 'причем', 'пускай', 'пусть', 'раз', 'разве', 'ровно', 'сиречь',
        'словно', 'так', 'также', 'тоже', 'только', 'точно', 'хоть', 'хотя', 'чем', 'чисто', 'что', 'чтоб', 'чтобы',
        'чуть',
        'якобы'
    )

    def __init__(self, text: str):
        self.raw_text = text

        self.sentences_count = text.count('.') + text.count('?') + text.count('!')

        text = text.replace('\n', ' ')

        for mark in self.PUNCTUATION_MARKS:
            text = text.replace(mark, '')

        self.cleared_text = text.strip().lower()

        self.words = tuple(word for word in self.cleared_text.split(' ') if word)
        self.unique_words = set(self.words)

        self.words_count = len(self.words)

    def get_lexical_diversity(self) -> float:
        """Лексическое разнообразие"""
        return len(self.unique_words) / self.words_count

    def get_syntactic_complexity(self) -> float:
        """Синтаксическая сложность"""
        return 1 - (self.sentences_count / self.words_count)

    def get_coefficient_of_speech_connectivity(self) -> float:
        """Коэффициент связности речи"""
        prepositions_count = 0
        unions_count = 0

        for preposition in self.PREPOSITIONS:
            prepositions_count += self.cleared_text.count(preposition)

        for union in self.UNIONS:
            unions_count += self.cleared_text.count(union)

        return (prepositions_count + unions_count) / (3 * self.sentences_count)

    def get_exclusivity_index(self) -> float:
        """Индекс исключительности"""
        return len(self.unique_words) / self.words_count

    def get_concentration_index(self) -> float:
        """Индекс концентрации"""
        words_count_with_frequency_10_and_more = 0
        for word in self.words:
            if self.cleared_text.count(word) >= 10:
                words_count_with_frequency_10_and_more += 1

        return words_count_with_frequency_10_and_more / self.words_count


texts_to_test = (
    '''
    Эта книга адресована всем, кто изучает русский язык. Но состоит она не из правил, упражнений и учебных текстов. Для этого созданы другие замечательные учебники.
    У этой книги совсем иная задача. Она поможет вам научиться не только разговаривать, но и размышлять по-русски. Книга, которую вы держите в руках, составлена из афоризмов и размышлений великих мыслителей, писателей, поэтов, философов и общественных деятелей различных эпох. Их мысли - о тех вопросах, которые не перестают волновать человечество.
    Вы можете соглашаться или не соглашаться с тем, что прочитаете в этой книге. Возможно, вам покажется, что какие-то мысли уже устарели. Но вы должны обязательно подумать и обосновать, почему вы так считаете.
    А еще вы узнаете и почувствуете, как прекрасно звучат слова любви, сострадания, мудрости и доброты на русском языке.
    ''',
    '''
    Как далеко ты от меня! Там, в сказочном Париже, танцуешь на величественной театральной сцене на Елисейских полях.
    Я хорошо знаю это, и все же мне кажется, что в ночной тишине я слышу твои шаги, вижу твои глаза, которые блестят, словно звезды на зимнем небе.
    Сегодня твой черед. Танцуй! Я танцевал в широких рваных штанах, а ты танцуешь в шелковом наряде принцессы.
    Эти танцы и гром аплодисментов порой будут возносить тебя на небеса. Лети! Лети туда! Но спускайся и на землю! Ты должна видеть жизнь людей, жизнь тех уличных танцовщиков, которые пляшут, дрожа от холода и голода. Я был таким, как они, Джеральдина.
    ''',
)

q1 = QuantitativeSpeechAssessments(texts_to_test[0])
q2 = QuantitativeSpeechAssessments(texts_to_test[1])

print('Case 1:\n',
      'lexical_diversity: ', q1.get_lexical_diversity(),
      '\n syntactic_complexity: ', q1.get_syntactic_complexity(),
      '\n coefficient_of_speech_connectivity: ', q1.get_coefficient_of_speech_connectivity(),
      '\n exclusivity_index: ', q1.get_exclusivity_index(),
      '\n concentration_index: ', q1.get_concentration_index()
      )

print('\n\nCase 2:\n',
      'lexical_diversity: ', q2.get_lexical_diversity(),
      '\n syntactic_complexity: ', q2.get_syntactic_complexity(),
      '\n coefficient_of_speech_connectivity: ', q2.get_coefficient_of_speech_connectivity(),
      '\n exclusivity_index: ', q2.get_exclusivity_index(),
      '\n concentration_index: ', q2.get_concentration_index()
      )
