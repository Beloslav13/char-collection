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

    # TODO: возможно стоит сделать не статический выбор по длинне пароля, а давать пользователю выбирать длину < 20.
    def generator(self, count=6):
        """
        Password generator returning a password string.
        :param count: int (6, 8 or 12)
        :return: '' <= random string of characters
        """
        collect_chars = self._collect_char
        random.shuffle(collect_chars)
        if count == 6:
            random.shuffle(collect_chars)
            return ''.join(collect_chars[:6])
        elif count == 8:
            random.shuffle(collect_chars)
            return ''.join(collect_chars[:8])
        elif count == 12:
            random.shuffle(collect_chars)
            return ''.join(collect_chars[:12])
        else:
            raise ValueError('Value can only be 6, 8 or 12')


if __name__ == '__main__':
    generator = GeneratorPassword()
    print('First password:', generator.generator())
    print('Second password:', generator.generator(8))
    print('Third password:', generator.generator(12))
    print('Error checking', generator.generator(13))