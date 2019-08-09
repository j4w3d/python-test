# Python code to check if two strings are 
# anagram 
 
from collections import Counter 
 
 
 
def anagram(input1, input2): 
 
 
 
    # Counter() returns a dictionary data 
 
    # structure which contains characters  
 
    # of input as key and their frequencies 
 
    # as it's corresponding value 
    dict1 = Counter(input1)
    dict2 = Counter(input2)
 
    print(dict1,"\n",dict2)
 
    return dict1 == dict2
 
 
# Driver function 
 
if __name__ == "__main__": 
 
    input1 = 'abccdd'
 
    input2 = 'dcacdb'
 
    print anagram(input1, input2) 
