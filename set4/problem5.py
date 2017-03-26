# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 00:07:26 2016

@author: ruialberto
"""

"""
Problem 5 - Playing a Hand 
"""

def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    # BEGIN PSEUDOCODE (download ps4a.py to see)
    total_pontos = 0
    total_letras = calculateHandlen(hand)
    
    # As long as there are still letters left in the hand:
    while total_letras >= 0:
        if total_letras == 0:
            print ("Run out of letters. Total score: ", total_pontos, "points.")
            break
    
        # Display the hand
                
        print("Current Hand: ", end="")
        displayHand(hand)
        guess = input('Enter word, or a "." to indicate that you are finished: ')
        
        # If the input is a single period:
        if guess == '.':
            print ("Goodbye! Total score:", total_pontos, "points.")
            # End the game (break out of the loop)
            break
        # Otherwise (the input is not a single period):
        else:
            is_valid = isValidWord(guess, hand, wordList)
            # If the word is not valid:
            if is_valid == False:
                # Reject invalid word (print a message followed by a blank line)
                print("Invalid word, please try again.")  
                print()
            # Otherwise (the word is valid):
            else:
                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                total = getWordScore(guess, n) 
                total_pontos = total_pontos + total
                print ('"%s"'%guess,' earned ', total, ' points. Total: ', total_pontos, ' points ')
                print ()
                # Update the hand
                hand = updateHand(hand, guess)
                total_letras = calculateHandlen(hand)
                total_letras = calculateHandlen(hand)