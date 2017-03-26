# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 00:31:33 2016

@author: ruialberto
"""

"""
Problem 4 - Decrypt a Story 
"""

def decrypt_story():
    try: 
        my_text = get_story_string()
        #print (my_text)
    except IOError:
        print ("A funçapo get_story_string nao funcionou!")
    
   
    cypher_object = CiphertextMessage(my_text)
    return cypher_object.decrypt_message()
    