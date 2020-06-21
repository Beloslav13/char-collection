import random

from char_collection.collect import CharacterSequence


class CollectPassword(CharacterSequence):
    """
    A class generating a random password of different characters.
    """

    @staticmethod
    def _collect(length, collect_chars):
        if length == 6:
            random.shuffle(collect_chars)
            return ''.join(collect_chars[:6])
        elif 6 < length <= 20:
            random.shuffle(collect_chars)
            return ''.join(collect_chars[:length])
        else:
            raise ValueError('password length can be from 6 to 20 characters')


if __name__ == '__main__':
    generator = CollectPassword()
    print('First password [length=6]:', generator.collect())
    print('Second password [length=12]:', generator.collect(12))
    print('Third password [length=15]:', generator.collect(15))
    print('Error checking [length=1]:', generator.collect(1))
    print('Error checking [length=25]:', generator.collect(25))
    print('Generator call as a function [length=6]:', generator())
    print('Generator call as a function [length=11]:', generator(11))
    print('Generator call as a function [length=17]:', generator(17))
