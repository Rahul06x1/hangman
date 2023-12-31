import random
import string

NEXT_ACTION = 'next_action'
GAME_OVER = 'game_over'
GAME_WON = 'game_won'
HANGMANPICS = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''',r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========''', ]

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
    if guess in guesses:
        print('You have already guessed that.')
        return guesses, chances, NEXT_ACTION
    guesses.append(guess)
    if guess not in secret_word:
        chances -= 1
        if chances == 0:
            return guesses, chances, GAME_OVER
        return guesses, chances, NEXT_ACTION
    masked_word = mask_secret_word(guesses,secret_word)
    if masked_word == secret_word:
        return guesses, chances, GAME_WON
    return guesses, chances, NEXT_ACTION

def get_user_input(user_input):
    if len(user_input) == 1 and user_input in string.ascii_letters:
        return user_input.lower()
    return False

def main():
    action = NEXT_ACTION
    guesses = []
    secret_word = get_random_word()
    chances = 6
    while True:
        print(HANGMANPICS[chances])
        print(get_status(guesses,secret_word,chances))
        if action == GAME_OVER:
            print("Too bad... you lost. The word is", secret_word)
            break
        if action == GAME_WON:
            print("Hurray, you won. The word is", secret_word)
            break
        if action == NEXT_ACTION:
            while True:
                user_input = input("Enter an alphabet : ")
                guess = get_user_input(user_input)
                if guess:
                    break
               
            guesses, chances, action = play_around(guess,guesses,secret_word,chances)
            
    play_again = input("Do you wish to play again? [Y/N]")
    if play_again == 'y' or play_again == 'Y':
        main()
        

if __name__ == '__main__':
    main()