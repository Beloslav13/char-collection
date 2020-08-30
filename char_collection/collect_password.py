import random

from char_collection.collect import CharacterSequence


class CollectPassword(CharacterSequence):
    """
    A class generating a random password of different characters.
    """

    @staticmethod
    def _collect(length, collect_chars):
        length = int(length)
        if length == 6:
            random.shuffle(collect_chars)
            return ''.join(collect_chars[:6])
        elif 6 < length <= 20:
            random.shuffle(collect_chars)
            return ''.join(collect_chars[:length])
        else:
            raise ValueError('password length can be from 6 to 20 characters')


class CollectPasswordNotSpecialSymbol(CollectPassword):
    """
    A class that generates a password without special characters
    """

    @property
    def _collect_all_char(self):
        special_characters = self.SPECIAL_CHARACTERS.copy()
        for char in special_characters:
            if not char.isdigit():
                self.SPECIAL_CHARACTERS.remove(char)
        return super()._collect_all_char
