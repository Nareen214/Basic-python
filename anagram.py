a=input("Enter any string : ")
b=input("Enter string2 ")
a1="". join (i for i in a if i.isalnum)
b1="". join (i for i in b if i.isalnum)
a2=sorted(a1)
b2=sorted(a2)
if a2==b2:
    print("The given string is anagram")
else:
    print("The given string is not anagram")