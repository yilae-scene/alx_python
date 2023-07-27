# The function returns the length of a sentence and the first letter of a sentence.

def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        return (length , 'None')
    else:
        return (length , sentence[0])
        

