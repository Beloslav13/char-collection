import random


class GeneratorPassword:
    """
    A class generating a random password of different characters.
    """
    SPECIAL_CHARACTERS = list('!@#$%^&*()_=+[]{};:"\|,')
    CONTINUE_CHR = list(range(91, 97))
    ALPHABET_CHR = range(65, 123)

    def __init__(self):
        self.all_characters = []

    def __call__(self, length=6):
        return self.generator(length)

    @property
    def _collect_char(self):
        """
        Internal method returning a list of all characters.
        """
        for i in self.ALPHABET_CHR:
            if i in self.CONTINUE_CHR:
                continue
            self.all_characters.append(chr(i))
        self.all_characters.extend(self.SPECIAL_CHARACTERS)
        return self.all_characters

    def generator(self, length=6):
        """
        Password generator returning a password string.
        :param length: 6 <= int <= 20
        :return: '' <- random string of characters
        """
        collect_chars = self._collect_char
        random.shuffle(collect_chars)
        try:
            result = self._generator(length, collect_chars)
        except ValueError:
            return 'password length can be from 6 to 20 characters'
        else:
            return result

    @staticmethod
    def _generator(length, collect_chars):
        if length == 6:
            random.shuffle(collect_chars)
            return ''.join(collect_chars[:6])
        elif 6 < length <= 20:
            random.shuffle(collect_chars)
            return ''.join(collect_chars[:length])
        else:
            raise ValueError('password length can be from 6 to 20 characters')


if __name__ == '__main__':
    generator = GeneratorPassword()
    print('First password [length=6]:', generator.generator())
    print('Second password [length=12]:', generator.generator(12))
    print('Third password [length=15]:', generator.generator(15))
    print('Error checking [length=1]:', generator.generator(1))
    print('Error checking [length=25]:', generator.generator(25))
    print('Generator call as a function [length=6]:', generator())
    print('Generator call as a function [length=11]:', generator(11))
    print('Generator call as a function [length=17]:', generator(17))

