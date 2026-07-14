'''
name="jimmy kohen"
city="US"
message="""hello this is 
"multi line string """

print(f"name:{name} city:{city} msg:{message}  ")

print(name[0])
print(name[-1])
print(name[1:4])
print(name[::-1])

first="alex"
last="cary"
print(first+last)
print(first*5)



name="programming"
count=0
print(name)
value=input("Enter count value :")
# for a in range(len(name)):
#     if value == name[a]:
#        count+=1
#     else:
#         print("not present")
#         break    
# print(f"alphabet :{value} count:{count}")
for char in name:
     if char==value:
          count+=1
print(f"alphabet :{value} count:{count}")

#i=0
#while i<len(name):
#    print(name[i])
#    i+=1
#for i,v in enumerate(name):
#    print(i,v)


text="progrAmming"

vowel="aeiou|AEIOU"
count=0
for char in text:
    if char in vowel:
        count+=1
print(f"total vowel :{count}")

print(min("Blanka")) #minimum B because of ASCII code
print(max("Blanka"))
print(len("Blanka"))



first_name=input("Enter first name :")
last_name=input("Enter last name :")

print(f"Full name is {first_name} {last_name} length is {len(first_name+last_name)}")

'''

string="programming"
print(string[::-1],end="")