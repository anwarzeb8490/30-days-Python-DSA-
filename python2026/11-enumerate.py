"""
nums=[22,33,44,55,66]

for x,y in enumerate(nums):
    print(f"index :{x}, value :{y}")

#even number with index

numbers=[22,33,44,55,66]

for x,y in enumerate(numbers):
    if x%2==0:
        print(f"index :{x} value :{y}")


num=[1,3,4,5,55,66,3,7,8]
max=0

for i in num:
    if i>=max:
        max=i
print(f"max :{max}")


#for negative values

num=[-1,-3,-4,-5,-55,-66,-3,-7,-8]
max=float("-inf")

for i in num:
    if i>=max:
        max=i
print(f"max :{max}")


number=[1,2,3,43,45,6,65,34,7,8]

def tag_exist(number,value):
    
    if value in number:
        return True
    else:
        return False
value=100
print(tag_exist(number,value))

number=[1,2,3,43,45,6,65,34,7,8]
def tag_exist(number,value):
    for num in number:
        if num==value:
            return True
    else:
        return False
value=45
print(tag_exist(number,value))



def sum_of_two_list(lst1,lst2):

    new_list=[]
    
    for i in range(0,len(lst1)):
        total=lst1[i]+lst2[i]
        new_list.append(total)
    return new_list


lst1=[2,3,4,5,6,7]
lst2=[3,4,5,5,6,4]
print(sum_of_two_list(lst1,lst2))

"""
newlst=[1,3,4,5,3,23,4]
#newlst=[1,2,3,3,4,5]

def chec_sorted(newlst):
    
    for i in range(0,len(newlst)-1):

        if newlst[i]>newlst[i+1]:
            return False
        
    return True

print(chec_sorted(newlst))