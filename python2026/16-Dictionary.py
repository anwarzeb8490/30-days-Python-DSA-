"""
marks={
    "math":88,
    "physics":77,
    "english":99,
    33:333,
    101:"mark",
    "abc":[1,2,3,4]
}
print(type(marks))
print(marks)
print(f"maths marks :{marks["math"]}")
print(marks.get("physics"))
print(marks.get("chemistry",0)) # will return non if key no in dictionary


marks={
    "math":88,
    "physics":77,
    "english":99,
}
print(marks)

k="english"
ans=marks.get(k)

if ans is None:
    print("subject not found")
else:
    print(f"subject is {ans} :")


# add and update keys

student={
    "name":"mark",
    "age":90
}
print(student)
print("id",id(student))
student["name"]="anthony"
student["gender"]="male"

print("id",id(student))
print(student)

# delete key

print(student.pop("gender"))
print(student)
del student["age"] #del student will delete  dictionary
student.clear()  # it will empty dictionary
print(student)

# dictionary is case sensitive 
student={
    "name":"mark",
    "age":90,
    "city":"ISB"
}

print("name" in student)
print("gender" not in student)

k=input("ENTER key :")
if k in student:
    print(student[k])
else:
    print("key not present")

"""
#dictionary methods

student={
    "name":"mark",
    "age":90,
    "city":"ISB"
}

student.update({"address":"H 90","age":24})
print(student)
print("age",student.get("age"))
print("gender",student.get("gender",0)) #without 0 give none
print(student.keys())
print(student.items())
print(student.values())


