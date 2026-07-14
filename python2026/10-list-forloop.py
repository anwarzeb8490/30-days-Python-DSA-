"""
name=["jack","hammer","corolla"]

print(name)
print(type(name))

marks1=[10,20,30,40,50]
marks2=[23,4,3,1,3]

#print(marks1*3) # print marks 3 times

print(marks1+marks2) #both list add


# built in functions
marks=[34,5,2,23,35]

n=len(marks)
maxi=max(marks)
mini=min(marks)
total=sum(marks)
sort=sorted(marks)
print(f"before list :{marks}")
print(f"Length : {n}")
print(f"Maximun : {maxi}")
print(f"minimum : {mini}")
print(f"total :{total}")
print(f"Sorted list :{sort}")
print(f"After list :{marks}")


#list indexing
fruits=["apple","banana","grapes","water_melon"]

print(fruits[0])
print(fruits[2])
print(fruits[-1])
print(fruits[-4])
print(fruits[len(fruits)-1])


lst=[1,2,3,4,5,6,7,8,9]

n=len(lst)
print(f"mini : {min(lst)}")
print(f"maxi : {max(lst)}")
print(f"middle : {lst[n//2]}")#for even list {lst[n//2-1]}

list1=[10,20,30,40,50]

list1[0]=11
list1[3]=33

print(list1)


#slicing
number=[1,2,3,4,5,6,7,8,9,10]

print(number[:2])

print(number[1:6])
print(number[::2])
print(number[len(number):6:-1])
print(number)
print(number[::-1])

cars=["farari","corolla","suzuki","BYD","toyota"]

for car in cars:
    print(car,end=" ")

i=0
while i<len(cars):
    print(cars[i],end=" ")
    i+=1
"""
cars=["farari","corolla","suzuki","BYD","toyota"]

for i in range(0,len(cars)):
    print(cars[i],end=" ")
print()
for car in cars[::-1]:
    print(car,end=" ")




