# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 00:21:17 2016

@author: ruialberto
"""

"""
Problem 1 - Build the Shift Dictionary and Apply Shift 
"""

class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
        
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        assert (shift >=0 and shift < 26), "Error: 0 <= shift < 26"      
        
        self.dicionario = {}

        alfabeto = string.ascii_lowercase 
        
        alfabeto_alt = alfabeto[shift:] + alfabeto[:shift]
        
        for l in alfabeto:
            self.dicionario[l] = ''
            
        i = 0
        for l in sorted(self.dicionario):
            self.dicionario[l] = alfabeto_alt[i]
            i = i +1
                   
        for key in sorted(self.dicionario):
            x = str(key)
            y = str(self.dicionario[key])
            #print ("%s : %s" % (x.upper(),y.upper()))
            self.dicionario[x.upper()] = y.upper()
            #print ("%s : %s" % (x.upper(),y.upper()))
            
        return self.dicionario  
        
        

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        
        self.code =''
        self.alfabeto = self.build_shift_dict(shift)
        
        for w in self.message_text:
            if w in string.punctuation or w in string.digits or w==' ':
                self.code = self.code + w
            else:
                p = self.alfabeto[w]
                self.code = self.code + p
                
        return self.code