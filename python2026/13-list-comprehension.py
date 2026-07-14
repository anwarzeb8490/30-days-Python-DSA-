"""

even=[i for i in range(1,10) if i%2==0 ]
print(even)

sq=[i*i for i in range(1,10) ]
print(sq)

names=['mark','tom','harry','nick']

up=[name.upper() for name in names]
print(up)

numb=[i for i in range(1,11)]
print(numb)

def is_prime(num):
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    if count==2:
        return True
    return False
pri=[i for i in range(1,101) if is_prime(i)==True]
print(pri)

"""    

odd=[i*i for i in range(1,10) if i%2==1]
print(odd)

marks=[10,22,75,20,30,80,32,100,200,3,4]
new_marks=[i for i in marks if i>=75]
print(new_marks)