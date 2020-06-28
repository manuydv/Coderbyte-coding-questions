# Have the function LetterChanges(str) take the str parameter being passed and modify it using the following algorithm. Replace every letter in the string with the letter following it in the alphabet (ie. c becomes d, z becomes a). Then capitalize every vowel in this new string (a, e, i, o, u) and finally return this modified string. 

import numpy as np 

def LetterChanges(str):

  alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a']
  vowels = ['a', 'e', 'i', 'o', 'u', 'a']
  caps_vowels = ['A', 'E', 'I', 'O', 'U', 'A']

  str = str.split(" ")

  new2 = []
  for i in range(len(str)):
    i = str[i]
    length = len(list(i))
    data = []
    new = []
    for j in range(length):      
      if i[j].isalpha():
        index = alphabets.index(i[j])
        new = alphabets[index+1]
        if new in vowels:
          index = vowels.index(new)
          new = caps_vowels[index]
        else:
            new = new
      else:
        new = i[j]
      data.append(new)
    new2.append(''.join(data))
  
  new3 = []
  for j in range(len(new2)):
    new3.append(''.join(new2[j]))
  

  return ' '.join(new3)
 


# keep this function call here 
print(LetterChanges(input()))






