"""
for i in range(1,3):
    for j in range(1,5):
        print(f"outervalue {i}  inner value{j}")



for i in range(1,6):
    for j in range(1,6):
        print(j,end=" ")
    print()

# 1 2 3 4 5 
# 1 2 3 4 5 
# 1 2 3 4 5 
# 1 2 3 4 5 
# 1 2 3 4 5 


for i in range(1,6):
    for j in range(1,6):
        print(i,end=" ")
    print()

# 1 1 1 1 1 
# 2 2 2 2 2 
# 3 3 3 3 3 
# 4 4 4 4 4 
# 5 5 5 5 5



for i in range(5,0,-1):
    for j in range(1,6):
        print(i,end=" ")
    print()
# 5 5 5 5 5 
# 4 4 4 4 4 
# 3 3 3 3 3 
# 2 2 2 2 2 
# 1 1 1 1 1 




for i in range(1,6):
    for j in range(1,i+1):
        print("*",end="")
    print()

# *
# **
# ***
# ****
# *****

for i in range(6,0,-1):
    for j in range(i,0,-1):
        print("*",end="")
    print()

# ******
# *****
# ****
# ***
# **
# *




for i in range(1,6):
    for j in range(1,i+1):
        print("*",end="")
    print()
for j in range(4,0,-1):
    for j in range(j,0,-1):
        print("*",end="")
    print()

# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *



for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()

# 1
# 12
# 123
# 1234
# 12345


for i in range(1,6):
    for j in range(i,0,-1):
        print(j,end="")
    print()

# 1
# 21
# 321
# 4321
# 54321



for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()
# 12345
# 1234
# 123
# 12
# 1

for i in range(1,6):
    for j in range(5,i-1,-1):
        print(j,end="")
    print()
# 54321
# 5432
# 543
# 54
# 5


n=int(input("Enter number for rows :"))
for i in range(1,n+1):
    for j in range(n,i-1,-1):
        print(j,end="*")
    print()
# 5*4*3*2*1*
# 5*4*3*2*
# 5*4*3*
# 5*4*
# 5*



for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end="")
    print()

# 54321
# 4321
# 321
# 21
# 1


for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()
for i in range(4,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()

# 1
# 12
# 123
# 1234
# 12345
# 1234
# 123
# 12
# 1


for i in range(5,0,-1):
    for j in range(5,i-1,-1):
        print(j,end="")
    print()
for i in range(2,6):
    for j in range(5,i-1,-1):
        print(j,end="")
    print()

# 5
# 54
# 543
# 5432
# 54321
# 5432
# 543
# 54
# 5


for i in range(1,6):
    for k in range(1,6-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    print()

#         1 
#       1 2 
#     1 2 3 
#   1 2 3 4 
# 1 2 3 4 5 

for i in range(5,0,-1):
    for k in range(1,i):
        print("@",end=" ")
    for j in range(5,i-1,-1):
        print(j,end=" ")
    print()

# @ @ @ @ 5 
# @ @ @ 5 4 
# @ @ 5 4 3 
# @ 5 4 3 2 
# 5 4 3 2 1 

"""
for i in range(1,6):
    for j in range(1,5-i+1):
        print("@",end=" ")
    for k in range(1,(i*2)-1+1):
        print(k,end=" ")
    print()
for i in range(4,0,-1):
    for j in range(1,5-i+1):
        print("@",end=" ")
    for k in range(1,(i*2)-1+1):
        print(k,end=" ")
    print()