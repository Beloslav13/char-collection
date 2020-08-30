# CharCollection

With this module you can easily generate a sequence from 1 to 75 characters, including special characters ``(!@#$%^&*()_=+[]{};:"\|,).``
This is a stand-alone module, from dependencies , only built-in random module (for now).

There is also a class for **generating a password** from characters from 6 to 20, including special characters.

## Simple use case:
<pre>
from char_collection.collect import CharacterSequence

collect = CharacterSequence()
collect.collect(10) # Q#,PT^$o&W (random string)
</pre>

## Or you can generate a password like this:
<pre>
from char_collection.collect_password import CollectPassword
generator = CollectPassword()
generator.collect(8) # B|Gd";;b
</pre>

## You can also use the CollectPasswordNotSpecialSymbol class, which will generate a password without special characters
<pre>
from char_collection.collect_password import CollectPasswordNotSpecialSymbol
generator_not_special_symbol = CollectPasswordNotSpecialSymbol()
generator_not_special_symbol.collect(8) # L3nAIorm
</pre>

**You can use the password generator, for example, in a telegram bot by connecting this module with the bot. 
Password must be at least 6 and no more than 20 characters.
If the length is false, returns None.**
