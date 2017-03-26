# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 00:30:26 2016

@author: ruialberto
"""

"""
Problem 3 - CiphertextMessage 
"""

class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
               
        Message.__init__(self, text)
                
            
    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        self.t = tuple()
        max_conta = 0
        str_final = ''
        final_shift = 0
        for i in range(26):  
            lista = []
            str_tmp = ''
            
            conta = 0
                        
            str_tmp = str_tmp + self.apply_shift(i)
            lista = str_tmp.split(' ')
            #tamanho = len(lista)
            #print ("Tamanho = ", tamanho)
            for f in lista:
                #print ("Palavra %s" %f)
                #print ("Shift: ", i)
                if is_word(self.get_valid_words(), f):
                    conta = conta + 1
            #print ("Conta = ",conta)        
            if conta > max_conta:
                max_conta = conta
                final_shift = i
                str_final = ''
                str_final = str_final + str_tmp
        
        self.t = (final_shift, str_final)
            
        return self.t
        