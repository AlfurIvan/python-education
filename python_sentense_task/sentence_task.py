"""Sentence task. Iterators, generators, RE, and pain"""
import re


class MultipleSentenceError(Exception):
    """class to explain Multiple Sentence Error`s plot"""
    def __init__(self, message="Many sentences"):
        self.message = message
        super().__init__(self, message)


class SentenceIterator:
    """Realization of Iterator Protocol, use iter() to switch between generator and iterator"""
    def __init__(self, stack_of_words):
        self.stack_of_words = stack_of_words
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index == len(self.stack_of_words.split(' ')):
            raise StopIteration
        return list(re.split('\\W+', self.stack_of_words))[self.index]


class Sentence:
    """This is base class, which contains validator _validate() , generator _words() and other"""
    def __init__(self, sentence):
        self.stack_of_words = self._validate(sentence=sentence)
        self.index = -1

    @classmethod
    def _validate(cls, sentence: str):
        """validator, which contains 3 tests and rises concrete Error for concrete sick"""
        if not isinstance(sentence, str):
            raise TypeError
        if sentence[-1] not in ('.', '?', '!'):
            raise ValueError
        if re.split(r'[.{3|1}?!]', sentence, maxsplit=1)[1] != '':
            raise MultipleSentenceError

        return sentence

    def _words(self):
        """generator(lazy, like me sometimes)"""
        self.index += 1
        if self.index == len(re.split(r'\W+', self.stack_of_words)):
            return   # raise StopIteration
        yield re.split(r'\W+', self.stack_of_words)[self.index]

    def __iter__(self):
        return SentenceIterator(self.stack_of_words)

    def __getitem__(self, key):
        if isinstance(key, slice):
            return ' '.join(re.split(r'\W+', self.stack_of_words)[key])
        return ''.join(re.split(r'\W+', self.stack_of_words)[key])

    def __repr__(self):
        """repr actually, returns <Sentence(words= , other_chars= )>"""
        return f'<Sentence(words={len(self.words())}, other_chars={len(self.other_chars())})>'

    def words(self):
        """return words for __repr__()"""
        return re.split(r'\W+', self.stack_of_words)

    def other_chars(self):
        """return other no space symbols for __repr__()"""
        return re.split(r'\w+', self.stack_of_words)


iter_ = iter(Sentence('Hello, word!'))
# print(Sentence('Hello world, ones, upon time!')[:])
# print(Sentence('Hello world, ones, upon time!').words())
for word in Sentence('Hello world!'):
    print(word)


print(next(iter_))
print(next(iter_))
# print(next(Sentence('Hello word!')._words()))
# for word in Sentence('Hello word,., pin!'):
#     print(word)
WTF = 'Idiot- wanna, drink some coffee?'
iter_2 = iter(Sentence(WTF))
print(iter_2)

print(next(iter_2))
print(next(iter_2))
print(next(iter_2))
print(next(iter_2))
print(next(iter_2))
