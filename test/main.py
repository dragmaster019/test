# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

import string



def count_words(sentence):
    sentence= sentence.translate(str.maketrans('','',string.punctuation))
    
    words= sentence.split()


    word_count= {}
    
   
    
    
    for word in words:
        word= word.lower()
        if word in word_count:
            word_count[word]+=1
        else:
            word_count[word]=1

    return word_count 
        
        
    
    
sentence="Hello, world! This is a test. Hello, world!"
print(count_words(sentence))