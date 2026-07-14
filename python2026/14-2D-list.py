"""
two_dmatrix=[[1,2,3],[11,22,33],[22,33,44]]

print(two_dmatrix[1][1])

for i in range(0,len(two_dmatrix)):
    for j in range(0,len(two_dmatrix)):
        print(two_dmatrix[i][j],end=" ")
    print()


two_dmatrix=[[1,2,3],[1,2,3],[1,2,3]]
total=0
for i in range(0,len(two_dmatrix)):
    for j in range(0,len(two_dmatrix)):
        
        total+=two_dmatrix[i][j]
    print(total,end=" ")
    print()
print(total)


matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9],
]

for i in range(0,len(matrix)):
    for j in range(0,len(matrix[0])):
        if i>=j :
            print(matrix[i][j],end=" ")
        else:
            print("*",end=" ")
    print()

# 1 * * 
# 4 5 * 
# 7 8 9 

matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9],
]

for i in range(0,len(matrix)):
    for j in range(0,len(matrix[0])):
        if i>j :
            print("*",end=" ")
        else:
            print(matrix[i][j],end=" ")
            
    print()

# 1 2 3 
# * 5 6 
# * * 9 


matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9],
]

for i in range(0,len(matrix)):
    for j in range(0,len(matrix[0])):
        if i==j :
            print("*",end=" ")
        else:
            print(matrix[i][j],end=" ")
            
    print()

# * 2 3 
# 4 * 6 
# 7 8 *



matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9],
]
print(len(matrix))

for i in range(0,len(matrix)):
    for j in range(0,len(matrix[0])):
       
        if i+j==len(matrix)-1:
            print(matrix[i][j],end=" ")
        else:
            print("*",end=" ")
    print()

"""

matrix=[
    [1,2,3,4],
    [4,5,6,4],
    [7,8,9,3],
    [7,8,9,3],
]

for i in range(0,len(matrix)):
    for j in range(0,len(matrix[0])):
        #if i==0 or i==3 or j==0 or j==3:
        if i in (0,3) or j in (0,3):
            print(i,j ,end="\t")
        else:
            print("*",end="\t")
    print()