import random

NEXT_ACTION = 'next_action'

def get_random_word(wordlist="/usr/share/dict/words"):
    good_words = []
    with open(wordlist) as f:
        words = [x.strip() for x in f]
        for word in words:
            if not word.isalpha(): # if there is punctuation
                continue
            if not word.islower(): # if it is a proper noun
                continue
            if len(word) < 5: # Too short
                continue
            good_words.append(word)

        secret_word = random.choice(good_words)
        return secret_word

def mask_secret_word(guesses,secret_word):
    masked_word = []
    for sw in secret_word:
        if sw in guesses:
            masked_word.append(sw)
        else:
            masked_word.append('-')
    masked_word = "".join(masked_word)
    return masked_word

def get_status(guesses,secret_word,chances):
    masked_word = mask_secret_word(guesses,secret_word)
    status = f"""SECRET WORD : {masked_word}
    Turns remaining : {chances}
    Guesses so far : {"".join(guesses)}
    """
    return status

def play_around(guess,guesses,secret_word,chances):
    if guess in secret_word:
        guesses.append(guess)
        return guesses, chances, NEXT_ACTION
