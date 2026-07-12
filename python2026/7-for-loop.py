"""
for i in range(1,10):
    print(i,end=" ")


#steps in for loop
for i in range(1,11,2):
    print(i,end=" ")


for i in range(10,0,-1):
    print(i,end=" ")

start=int(input("Enter start value :"))
end=int(input("Enter end value :"))

for i in range(start,end+1):
    if i%2==0:
        print(i,end=" ")

start=int(input("Enter start value :"))
end=int(input("Enter end value :"))
sum=0
for i in range(start,end+1):
    sum+=i
print(sum)



num=1
while num<=10:

    if num==5:
        break
    print(num)
    num+=1


for i in range(1,11):
    if i==8:
        break
    elif i==5:
        continue

    print(i,end=" ")

"""



sum=0
while True:
    value=int(input("Enter value :"))
    if value>=1:
        sum+=value
    elif value<0:
        continue
    else:
        break
print(f"total positive values sum is {sum}")
