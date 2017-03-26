# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 00:10:21 2016

@author: ruialberto
"""

"""
Problem 7 - You and your Computer 
"""

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
          But if no hand was played, output "You have not played a hand yet. 
          Please play a new hand first!"
        
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    while True:
         #tamanho = HAND_SIZE
         #mao = dealHand(tamanho)
         resposta = input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
         if resposta == 'n':
            while True:
                 resposta2 = input('Enter u to have yourself play, c to have the computer play: ')
                 tamanho = HAND_SIZE
                 mao = dealHand(tamanho)
                 if resposta2 == 'u':
                      playHand(mao, wordList, tamanho)
                      break
                 elif resposta2 == 'c':
                       compPlayHand(mao, wordList, tamanho)
                       break
                 else:
                     print ('Invalid command.')
         elif resposta == 'r':
               while True:
                         try:
                            len(mao) > 0
                            resposta3 = input('Enter u to have yourself play, c to have the computer play: ')
                            if resposta3 == 'u':
                                    playHand(mao, wordList, tamanho)
                                    break
                            elif resposta3 == 'c':
                                    compPlayHand(mao, wordList, tamanho)
                                    break
                            else:
                                    print ('Invalid command.')
                         except:
                                print ('You have not played a hand yet. Please play a new hand first!')
                                break
         elif resposta == 'e':
                  break
         else:
                print ('Invalid command.')
