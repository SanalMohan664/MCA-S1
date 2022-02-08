#a
list=[25,-12,-2,54,-32,24,-53,46,-5,-67,-78,8,95]
positive=[x for x in list if x>0]
print(positive)

#b
n=int(input("Enter the limit: "))
sq=[x*x for x in range(n+1)]
print(sq)

#c
word=input("Enter a word: ")
vowel=["A","E","I","O","U","a","e","i","o","u"]
list_v=[x for x in word if x in vowel ]
print(list_v)

#d
word=input("Enter a word: ")
list_o=[ord(x) for x in word]
print(list_o)
