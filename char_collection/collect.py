import random


class CharacterSequence:
    """
    A class generating a random password of different characters.
    """
    SPECIAL_CHARACTERS = list('!@#$%^&*()_=+[]{};:\\"|,1234567890')
    CONTINUE_CHR = list(range(91, 97))
    ALPHABET_CHR = range(65, 123)

    def __init__(self):
        self.all_characters = []

    def __call__(self, length=6):
        return self.collect(length)

    @property
    def _collect_all_char(self):
        """
        Internal method returning a list of all characters.
        """
        for i in self.ALPHABET_CHR:
            if i in self.CONTINUE_CHR:
                continue
            self.all_characters.append(chr(i))
        self.all_characters.extend(self.SPECIAL_CHARACTERS)
        return self.all_characters

    def collect(self, length=6):
        """
        A collection that returns a string of random characters.
        :param length: 0 <= int <= 75
        :return: '' <- random string of characters
        """
        random.shuffle(self._collect_all_char)
        try:
            result = self._collect(length, self._collect_all_char)
        except ValueError:
            return None
        except TypeError:
            return None
        else:
            return result

    @staticmethod
    def _collect(length, collect_chars):
        length = int(length)
        if length == 6:
            random.shuffle(collect_chars)
            return ''.join(collect_chars[:6])
        elif 0 < length <= 75:
            random.shuffle(collect_chars)
            return ''.join(collect_chars[:length])
        else:
            raise ValueError('length can be from 1 to 75 characters')
