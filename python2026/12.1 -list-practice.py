"""
lst=[-3,-2,-1,-4,-5,-63,-54,-5]

def minimum(lst):
    mini=float("-inf")
    for i in lst:
        if i>mini:
            mini=i
    return mini

print(minimum(lst))



def reverse_lst(lst):
    newlst=[]
    n=len(lst)
    for i in range(n-1,-1,-1):
        newlst.append(lst[i])
    return newlst

lst=[1,2,3,4,5,31,3]
print(lst)
print(reverse_lst(lst))


#def merge(lst1,lst2):
#    return lst1+lst2
def merge(lst1,lst2):

    new_list=[]
    for i in lst1:
        new_list.append(i)
    for j in lst2:
        new_list.append(j)
    return new_list

lst1=[1,2,3,4]
lst2=[5,6,7,8]

print(merge(lst1,lst2))



def remove_dup(lst):
    result=[]

    for i in lst:
        if i not in result:
            result.append(i)
    return result

lst=[1,2,3,3,7,7,4,5,5,6,6,7,7,8,9,1]

print(remove_dup(lst))


def even_odd(lst):
    eve=[]
    odd=[]
    for i in lst:
        if i%2==0:
            eve.append(i)
        else:
            odd.append(i)
    return eve,odd

lst=[1,2,3,4,5,6,7,8,9,20]

res=even_odd(lst)
print(res)


def seq(lst):
    sqlst=[]
    
    for i in lst:
        sqlst.append(i*i)
    return sqlst

lst=[1,2,3,4,5]
print(lst)
print(seq(lst))




lst=[1,1,1,1,1,1,1,2,2,3,4,5,6,1,1,7,8,4,9,20]


#
# def remove_occurance(lst,target):
#     new_list=[]
#     for num in lst:
#         if num!=target:  # if num==target:
#             new_list.append(num) #lst.remove(num) it wont work it will stuck in loop
#     return new_list
# r_o=remove_occurance(lst,1)
# print(r_o)
#other method
def remove_occurance1(lst,target):
    while target in lst:
        lst.remove(target)
        
    return lst
print(remove_occurance1(lst,1))


"""

lstneg=[1,3,4,5,-13,4,5,-2,45,-8,-10000]


def negative_num(lstneg):
    for i in range(0,len(lstneg)):
        if lstneg[i]<0:
            lstneg[i]=0
    return lstneg
print(negative_num(lstneg))

