It relies on `/usr/share/dict/words` for random words. 

The purpose is to teach test driven development.

Logic

1. Get a random word
2. Mask the word
3. Get user input
4. Check if input is there in secret word
5. If yes:
6.    unmask all occurrences of letter
7.    Add to guesses
8. else:
9.    increase wrong guesses counter
10.   Add to guesses
