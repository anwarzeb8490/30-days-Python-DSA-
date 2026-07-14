"""

#CASE conversion

#upper()
#lower()
#capitalize()
#title()
#swapcase()

text="proGramMing python"

print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title())
print(text.swapcase())

#check content give T/F
# isalpha()
# isspace()
# isalnum()
# isdigit()
# startswith()
# endswith
text="python programming"
print(text)
print("alphabet :",text.isalpha()) #if space will give False
print("space :",text.isspace()) # check white space not space
text1="abc123"
print(text1)
print("check alpha numeric :",text1.isalnum()) # alphabet or digit or both return true
text3="213123"
print(text3)
print("check digit:",text3.isdigit()) # float give false
print("start with ",text3.startswith("2"))
print("End with ",text3.endswith("3"))

age=input("Enter your age :")

if age.isdigit():
    if int(age)>=18:
        print("you can vote")
    else:
        print("you cannot vote")
else:
    print("enter digit")


# count()
# find()
# index()
# replace()

sentence="python is great python programming language"
print(sentence.count("python"))
print(sentence.find("is")) # if not in sent give -1
print(sentence.index("is")) #if not give value error
print(id(sentence))
new_sent=sentence.replace("is","are") # not change real sentence give new one
print(new_sent)
print(sentence)
print(id(new_sent))



"""

# split and join


text="python  is programming language"
lst=text.split()
print(lst)
print(len(lst))

text_list=['python', 'is', 'programming', 'language']
lst1=" ".join(text_list)
print(lst1)
print(len(lst1))


text_prog=['python', 'is', 'programming', 'language',3]
new_text=" ".join(str(ch) for ch in text_prog)
print(new_text)
