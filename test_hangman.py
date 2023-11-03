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