#Have the function FirstReverse(str) take the str parameter being passed and return the string in reversed order. 
#For example: if the input string is "Hello World and Coders" then your program should return the string sredoC dna dlroW olleH.

def FirstReverse(str):

  str = str.split(" ")

  data = []
  new2 = []
  for i in range(len(str)):
    i = list(str[i])
    data = []
    for j in reversed(range(len(i))):
      data.append(i[j])
    new2.append(''.join(data))
  
  new3 = []
  for j in reversed(range(len(new2))):
    new3.append(''.join(new2[j]))



  return ' '.join(new3)
      

print(FirstReverse(input()))




== INPUT ==
"I Love Code"

== OUTPUT ==
edoC evoL I

<< CORRECT >>

== INPUT ==
"coderbyte"

== OUTPUT ==
etybredoc

<< CORRECT >>













