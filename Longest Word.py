#Have the function LongestWord(sen) take the sen parameter being passed and return the largest word in the string. If there are two or more words that are the same length, return the first word from the string with that length. Ignore punctuation and assume sen will not be empty. 

def LongestWord(sen):

 sen = sen.split(' ')

 count2 = []

 for i in sen:
   count = 0
   for j in range(len(i)):
     if i[j].isalpha():
       count = count + 1
   count2.append(count)
  

 return sen[count2.index(max(count2))]
 
print(LongestWord(input()))
