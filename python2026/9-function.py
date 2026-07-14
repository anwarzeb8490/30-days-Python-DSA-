"""
def even_odd():
    num=int(input("Enter number :"))
    if num%2==0:
        print("Even")
    else:
        print("odd")

even_odd()


def print_Factors():
    value=int(input("Enter number"))
    for i in range(1,value+1):
        if value%i==0:
            print(f"factors {i}",end=" ")
print_Factors()              



def add(a,b):
    return a+b

sum=add(2,4)
print(sum)


def greet(name):
    return f"hello {name}"

print(greet("anwar"))



def rectangle_area(l,b):
    print(f"Total area is {l+b}sqft")

rectangle_area(180,90)



def find_max(a,b,c):

    if a>(b and c):
        print(f"{a} is great then {b} and {c}")
    elif b>(a and c):
        print(f"{b} is great then {a} and {c}")
    else:
        print(f"{c} is great then {a} and {b}")

find_max(33,8,31)




def discount_price(o_price,dis_price):
    print(f"orignal price is {o_price} after discount {dis_price} total is {o_price-dis_price}")

discount_price(5000,300)




def is_prime(val):
    count=0
    for i in range(1,val+1):
        if val%i==0:
            count+=1
    if count==2:
        return True
    else:
        return False

print(is_prime(5))




name="anwar"

def greet(name):
    
    name="zeb"
    print(f"Hello {name}")

greet(name)
print("calling print :",name)

"""
age=lambda age: "you can vote" if age>18 else "you cannot vote"

print(age(90))