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
    word_scores = {}
    
    if len(word_list):
        for word in word_list:
            score = score_word(word)
            word_scores[word] = score
        top_score = max(word_scores.values())   
        top_words = [word for word, score in word_scores.items() if score == top_score]
        
        winning_word = top_words[0]
        if len(top_words) > 1:
            for word in top_words:
                # Case 1 
                # already found 10 letter word, don't want to replace it
                # check this case first to ensure a 10 letter word is not replaced with a shorter word
                if len(winning_word) == 10:
                    continue

                # Case 2 
                # found a 10 letter word that is longer than the currently stored winning word
                elif len(word) == 10 and len(winning_word) != 10:
                    winning_word = word

                # Case 3
                # winning_word is less than 10 letters and the current word is shorter
                elif len(word) < len(winning_word):
                    winning_word = word
                
                # Case 4 
                # the string held by winning_word is not 10 letters
                # and the current word is longer than winning word
                # no action needed 

    return (winning_word, top_score)