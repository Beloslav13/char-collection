# CharCollection

With this module you can easily generate a sequence from 1 to 75 characters, including special characters ``(!@#$%^&*()_=+[]{};:"\|,).``
This is a stand-alone module, from dependencies , only built-in random module (for now).

There is also a class for **generating a password** from characters from 6 to 20, including special characters.

## Simple use case:
<pre>
from char_collection.collect import CharacterSequence

collect = CharacterSequence()
result = collect.collect(10)
print(result)  # Q#,PT^$o&W (random string)
</pre>

## Or you can generate a password like this:
<pre>
from char_collection.collect_password import CollectPassword
generator = CollectPassword()
result = generator.collect(8) 
print(result) # B|Gd";;b
</pre>

**You can use the password generator, for example, in a telegram bot by connecting this module with the bot. 
Password must be at least 6 and no more than 20 characters.
If the length is false, returns None.**
