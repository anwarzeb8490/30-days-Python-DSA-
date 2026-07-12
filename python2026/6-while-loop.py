"""
count=1

while count<=5:
    print(f"{count} Hello")
    count+=1
    print(f"{count} done")

n=int(input("Enter number :"))

i=1
while i<=n:
    print(i ,end=" ")
    i+=1


start=int(input("Enter first value :"))
end=int(input("Enter second value :"))

while start<=end:
    print(start,end=" ")
    start+=1



start=int(input("Enter first value :"))
end=int(input("Enter second value :"))
while start<=end:
    if start%3==0 and start%4==0:
        print(start,end=" ")
    start+=1




i=10

while i>=1:
    print(i,end=" ")
    i-=1


num=1
while num <=100:
    if  num%3==0 and num%5==0:
        print(num,end=" ")
    num+=1

num=1
sum=0
while num<=10:
    sum+=num
    print(f"num :{num}, sum{sum}")
    num+=1

num=1
sum=0
while num<=100:
    if num%2==0 and num%7==0:
        sum+=num
        print(f"number {num} sum{sum} ")
    num+=1

    


table=int(input("Enter table num :"))
start=1
end=10
while start<=end:
    print(f"{table}*{start}={table*start}")
    start+=1



num=int(input("Enter number factorial"))
end=1
fact=1
while num>=end:
    fact*=num
    num-=1
print(fact)

"""
#factors of number

num=int(input("Enter number :"))

i=1
count=0
while i<=num:
    if num%i==0:
        count+=1
        print(f"factor are {i} total factor {count}")
    i+=1