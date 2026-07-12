"""
age =int(input("Enter your age :"))

if age>=18:
    print("you can vote")
    print("you are eligible")
else:
    print("you can not vote")



marks=75

if marks>=40:
    print("you have passed")
else:
    print("you are failed")




marks=int(input("Enter your marks"))

if marks>=91 and marks<=100:
    print("Grade A")
elif marks>=81 and marks <=90:
    print("B")
elif marks>=71 and marks <=80:
    print("C")
elif marks>=61 and marks <=70:
    print("D")
elif marks>=33 and marks <=60:
    print("Fail")
else:
    print("INVALID MARKS")


age=int(input("Enter your age: "))
has_certi=True

if age>=18:

    if has_certi:
        print("you can hire")
    else:
        print("Cannot hire due to no certificate")

else:
    print("cannot hire due to age limit age <18 ")


#ternanry if else

age=12

status="Adult" if age>=18 else "Minor"

print(f"status : {status}")


number=33

if number>=1:
    print("Positive number")
elif number <=-1:
    print("Negative number")
else:
    print("Zero number")

num1=3
num2=3
if num1>num2:
    print(f"Number {num1} is greater then {num2}")
elif num2 > num1 :
    print(f"Number {num2} is greater then {num1}")
else:
    print("Both are equal")


age=30
has_id=False

if age>=18:
    if has_id:
        print("you can enter")
    else:
        print("You dont have an ID card ")
else:
    print("You cannot enter")



a=31
b=8
c=44

if a>(b and c):
    print(f"{a} is greater then {b} and {c}")
elif b>(a and c):
    print(f"{b} is greater then {a} and {c}")
else:
    print(f"{c} is greater then {a} and {b}")

num=33

status="Even" if num%2==0 else "ODD"
print(f"Number {num} is {status}")



purchase=55000
discount=0

if purchase>=5000:
    discount=purchase-(purchase*0.20)
    print(f"Thank you for shopping {purchase} RS your Discount 20% your total bill {discount}RS")

elif purchase>=2000:
    discount=purchase-(purchase*0.10)
    print(f"Thank you for shopping {purchase} RS your Discount 20% your total bill {discount}RS")
elif purchase>1000:
    discount=purchase-(purchase*0.05)
    print(f"Thank you for shopping {purchase} RS your Discount 20% your total bill {discount}RS")
else:
    print(f"No discount your bill is {purchase}")
    


"""
# divisible by 4 and 400 but not 100
#200 not leapyear
#204 leap year
#400 leap year

year=200

if (year%4==0 and year%100 !=0 ) or year%400==0 :
    print(f"leap year is {year}")
else:
    print("not a leap year")


