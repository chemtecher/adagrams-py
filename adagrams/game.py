from itertools import repeat
import random

LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}

SCORE_CHART = {"A": 1, "E": 1, "I": 1, "O": 1, "U": 1, "L": 1, "N": 1 , "R": 1, "S": 1, "T": 1, "D": 2, "G": 2, "B": 3, "C": 3, "M": 3, "P":3, "F": 4, "H": 4, "V": 4, "W": 4, "Y": 4, "K": 5, "J": 8, "X": 8, "Q": 10, "Z": 10}

def draw_letters():
    letters = []
    letter_bank = []
    for letter,count in LETTER_POOL.items():
        letters.extend(repeat(letter, count))
    
    while len(letter_bank) < 10:
        random_letter = random.choice(letters)
        letter_bank.append(random_letter)
        letters.remove(random_letter)
    
    return letter_bank

def uses_available_letters(word, letter_bank):
    letter_bank_copy = letter_bank.copy()
    upper_word = word.upper()
    
    if len(upper_word) > len(letter_bank_copy):
        return False
    for letter in upper_word:
        if letter not in letter_bank_copy:
            return False
        else:
            letter_bank_copy.remove(letter)
    return True 

def score_word(word):
    
    score = 0
    
    for letter in word.upper():
        if letter in SCORE_CHART:
            score += SCORE_CHART[letter]

    if len(word) > 6:
        score += 8
    
    return score
    

def get_highest_word_score(word_list):
    pass