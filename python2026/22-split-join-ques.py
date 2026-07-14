# Reverse string
"""
text="python is programming language"

print(text)
words_list=text.split()
words_list=words_list[::-1]
text=" ".join(words_list)

print(text)

# email validation atleast @ and .

def check_email(email: str):
    if email.count("@")==1 and "." in email:
        return "valid"
    else:
        return "invalid"

email="abc@gmail.com"
ans=check_email(email)
print(ans)


# clean phone number

def clean_number(phone_number: str):
    clean=phone_number.replace("-","")
    final_clean=clean.replace("+92","")
    return final_clean

phone_number="+92-333-232234"
ans=clean_number(phone_number)
print(ans)

def count_vowel(sentence: str):
    vowel="aeiouAEIOU"
    count=0
    dictionary={}
    text=sentence.split()
    for word in text:
        if word[0] in vowel:
            count+=1
            dictionary[word]=count
        else:
            dictionary[word]=0
    return dictionary

sentence="The quick over brown fox jumps over the lazy dog"
ans=count_vowel(sentence)
print(ans)

# check file name .pdf .txt .py

filename="report.pdf"

if filename.endswith(".pdf") or filename.endswith(".txt") or filename.endswith(".py"):
    print(f"Valid file name {filename}")
else:
    print("invalid only support .pdf ,.txt ,.py")

# print longest word
sentence="The quick over brown fox jumps over the lazy dog"

def longest_word(sentence: str):
    words=sentence.split()
    count=0
    longest_word=""
    for word in words:
         if len(word) > count:
             count=len(word)
             longest_word=word
        #print(count ,text)
        #print(word,len(word))
    print(longest_word ,count)
ans=longest_word(sentence)
print(ans)


sentence="The quick over brown fox jumps over the lazy dog"

def longest_word(sentence: str):
    words=sentence.split()
    longest_word=max(words,key=lambda x:len(x))
    print(longest_word,len(longest_word))

ans=longest_word(sentence)
print(ans)


username=input("Enter user name")

clean=username.strip()
if clean[0].isdigit():
    print("Invalid user name")    
else:
    print("valid user name")


text=input("Enter word to check palindrome :")
text=text.strip()
if text== text[::-1]:
    print(f"{text} is palindrome")
else:
    print(f"{text} is not palindrome")


def reverse_order(text):
    #text=text.lower().replace(" ","")
    #return text ==text[::-1]
    text=text.split()
    rev=text[::-1]
    rev=" ".join(rev)
    return f"REverse Text :{rev}"
text="python is fun"
print("Text :",text)
ans=reverse_order(text)
print(ans)



def unique_count(text):
    text=text.split()
    unique_word=list()
    #print(len(set(text)))
    count=0
    for word in text:
        if word not in unique_word:
            unique_word.append(word)
            count+=1
    text=" ".join(unique_word)
    return f"unique words :{text}: count={count}"

text="python is is good python programming"
ans=unique_count(text)
print(ans)


"""

def word_count(text):
    words=text.split()
    new_list=[]
    for word in words:
        new_list.append((word,len(word)))
    
    result=" ".join(str(item) for tup in new_list for item in tup)
    print(result)


text="hello python is programming language"
ans=word_count(text)
print(ans)