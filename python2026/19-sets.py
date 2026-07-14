# unordered , unique , immutable element , no indexing
"""
my_set={"jim","tom","alex","diaz","alex"}

my_set1={4,5,4,5,5,64,34,}
print(len(my_set))
print(my_set)
print("jim" in my_set)

fruits={"banana","mango","apple"}
fruits.add("kiwi")
print(fruits)
fruits.remove("apple") #give error if not exist
print(fruits)
fruits.discard("appple") # no error if not exist
print(fruits)
fruits.pop() # random element remove
print(fruits)


a={1,2,3,4} 
b={3,4,5,6}
print(a & b) # intersection present in both
print(a.intersection(b)) # another method

print(a|b) # union
print(a.union(b)) #or union


"""
a={7,6,1,2,4,3,5,3}
print(a)

#for i in range(len(a)):
#    print(a[i])  # it wont work because of no indexing

for i,v in enumerate(a):
    print(i,v)