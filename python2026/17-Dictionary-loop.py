"""
marks={
    "english":44,
    "maths":66,
    "comp":34,
    "history":77
}
count=0
total=0
for k in marks.keys():
    count+=1
    total+=marks[k]
    print(f"student subject {k} and marks {marks[k]} ")
print(f"Total marks {total} and count {count}")

marks={
    "english":44,
    "maths":66,
    "comp":34,
    "history":77,
    "urdu":90,
    "physics":33
}
print(marks.items())
failed=0
pass_sub=0
for k,v in marks.items():
    if v>=80:
        print(f" subject {k} :{v} Excellent")
        pass_sub+=1
    elif v>=60:
        print(f" subject {k} :{v} Good")
        pass_sub+=1
    elif v>=50:
        pass_sub+=1
        print(f" subject {k} :{v} Fair")
    elif v>=35:
        pass_sub+=1
        print(f" subject {k} :{v} Need improvement")
    else:
        failed+=1
        print(f" subject {k} : failed")
print(f"Pass subject {pass_sub} Failed subject :{failed}")


student_profile={
    "name":"mark",
    "city":"london",
    "age":33,
    "marks":[33,44,55]
}

for k in student_profile.keys():
    print(f"{k}:{student_profile[k]}")


marks={
    "maths":55,
    "eng":44,
    "history":33
}
search_key="bio"
print(marks.get(search_key,"Not available"))

product={
    "milk":333,
    "bread":200,
    "sugar":250
}
pro=input("Enter product name :")

if pro in product:
    print(product[pro])
else:
    print("not present")
total=0
count=0
for k in product.values():
    total+=k
    count+=1
print(f"total : {total} Average :{total/count}")


students={
    "anthony":80,
    "mark":70,
    "david":50,
    "jim":60
}

for k,v in students.items():
    if v=70:
        print(f"{k} : {v}")


dict1={
    "a":1,
    "b":2,
}
dict2={
    "c":3,
    "d":4,
}
def merge(dict1,dict2):
    global dict3
    dict3={}
    dict3.update(dict1)
    dict3.update(dict2)
    return dict3
print(merge(dict1,dict2))
#print(dict1.update({dict2}))
print(len(dict3))


dict1={
    "a":1,
    "b":2,
}
dict2={
    "c":3,
    "d":4,
}
dict3={**dict1,**dict2}
print(dict3)



students={
    "101":{"name":"mark","age":23},
    "102":{"name":"jim","age":33},
    "103":{"name":"luke","age":43}
}
for student in students:
    
    for k,v in students[student].items():
        print(f"id:{student} = {k}:{v} ")
"""
students={
    "101":{"name":"mark","age":23},
    "102":{"name":"jim","age":33},
    "103":{"name":"luke","age":43}
}

for k,v in students.items():
    print("id :",k,v)
    print(f"id :{k}  name : {v["name"]}")