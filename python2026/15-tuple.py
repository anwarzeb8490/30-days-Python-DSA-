my_tuple=(1,2,3,1,1,2,2,33)

lst=list(my_tuple)
lst[0]=11
my_tuple=tuple(lst)
print(my_tuple)
print(my_tuple.index(11))
print(my_tuple.count(1))
print(my_tuple[0])
print(sum(my_tuple))
print(min(my_tuple))
print(max(my_tuple))
print(len(my_tuple))
print(sorted(my_tuple, reverse=True))


cart_tuple=("mazda","corolla","suzuki","Toyota")

for i,v in enumerate(cart_tuple):

    print (f"index : {i}  value : {v}")

