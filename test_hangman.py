import os
from hangman import *

def test_random_word_lowercase():
    fname = "/tmp/sample_wordlist"
    with open(fname, "w") as f:
        f.writelines(["Grape\n", "apple\n", "Mango\n"])
        
    for _ in range(100):
        assert get_random_word(fname) == "apple"

    os.unlink(fname)

def test_random_word_no_punctuation():
    fname = "/tmp/sample_wordlist"
    with open(fname, "w") as f:
        f.writelines(["pineapple\n", "mango's\n", '"beryl"'])

    for _ in range(100):
        assert get_random_word(fname) == "pineapple"
    
    os.unlink(fname)

def test_random_word_min_length_5():
    fname = "/tmp/sample_wordlist"
    with open(fname, "w") as f:
        f.writelines(["pineapple\n", "ape\n", 'dog\n', 'bear\n'])

    for _ in range(100):
        assert get_random_word(fname) == "pineapple"
        
    os.unlink(fname)

def test_mask_secret_word_no_guesses():
    guesses = []
    secret_word = 'tiger'
    masked_word = mask_secret_word(guesses,secret_word) 
    assert masked_word == '-----'

def test_mask_secret_word_single_correct_guess():
    guesses = ['i']
    secret_word = 'tiger'
    masked_word = mask_secret_word(guesses,secret_word) 
    assert masked_word == '-i---'

def test_mask_secret_word_single_wrong_guess():
    guesses = ['x']
    secret_word = 'tiger'
    masked_word = mask_secret_word(guesses,secret_word) 
    assert masked_word == '-----'

def test_mask_secret_word_two_correct_guesses():
    guesses = ['i','g']
    secret_word = 'tiger'
    masked_word = mask_secret_word(guesses,secret_word) 
    assert masked_word == '-ig--'

def test_mask_secret_word_one_correct_guess_multiple_occurance():
    guesses = ['x','p']
    secret_word = 'apple'
    masked_word = mask_secret_word(guesses,secret_word) 
    assert masked_word == '-pp--'

def test_get_status():
    guesses = ['x', 'p']
    secret_word = 'apple'
    chances = 7
    status = get_status(guesses,secret_word,chances)
    assert status == """SECRET WORD : -pp--
    Turns remaining : 7
    Guesses so far : xp
    """
def test_play_around_correct_guess():
    guesses = []
    guess = 'a'
    secret_word = 'apple'
    chances = 7
    guesses,chances,next_action = play_around(guess,guesses,secret_word,chances)

    assert chances == 7
    assert guesses == ['a']
    assert next_action == NEXT_ACTION

def test_play_around_wrong_guess_game_not_over():
    guesses = ['a']
    guess = 'x'
    secret_word = 'apple'
    chances = 7
    guesses,chances,next_action = play_around(guess,guesses,secret_word,chances)

    assert chances == 6
    assert guesses == ['a','x']
    assert next_action == NEXT_ACTION

def test_play_around_wrong_guess_game_over():
    guesses = ['a']
    guess = 'x'
    secret_word = 'apple'
    chances = 1
    guesses,chances,next_action = play_around(guess,guesses,secret_word,chances)

    assert next_action == GAME_OVER

def test_play_around_win():
    guesses = ['a','l','e']
    guess = 'p'
    secret_word = 'apple'
    chances = 1
    guesses,chances,next_action = play_around(guess,guesses,secret_word,chances)

    assert next_action == GAME_WON

def test_play_around_repeated_guess():
    guesses = ['a','l','e']
    guess = 'l'
    secret_word = 'apple'
    chances = 7
    guesses,chances,next_action = play_around(guess,guesses,secret_word,chances)

    assert chances == 7
    assert guesses == ['a','l','e']
    assert next_action == NEXT_ACTION

def test_get_user_input_single_charactor():
    user_input = 'a'
    user_input = get_user_input(user_input)
    assert len(user_input) == 1

def test_get_user_input_alphabet():
    user_input = 'a'
    user_input = get_user_input(user_input)
    assert user_input == 'a'

def test_get_user_input_invalid():
    user_input = '*'
    user_input = get_user_input(user_input)
    assert user_input == False