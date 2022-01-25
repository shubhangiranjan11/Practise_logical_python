name="shikha"
vowel=0
consonant=0
i=0
while i<len(name):
    if name[i]=="i" or name[i]=="e" or name[i]=="o" or name[i]=="u" or name[i]=="a":
        vowel+=1
    else:
        consonant+=1
    i+=1
print(vowel)
print(consonant)


# vowel="aeiou"
# name="shikha"
# i=0
# while i<len(vowel):
#     j=0
#     while j<len(name):
#         if vowel[i] == name[j]:
#             print(vowel[i])
#         j+=1
#     i+=1
