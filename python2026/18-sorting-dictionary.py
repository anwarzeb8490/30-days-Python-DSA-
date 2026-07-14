"""
marks={"math":40,"science":85 ,"english":45,"history":41}


x=dict(sorted(marks.items(),key=lambda x:x[1]))

print(x)

marks={
    "jim":[2,44,56,32,33],
    "alex":[44,55,88,55,65],
    "mark":[65,44,34,65,44],
    "jade":[67,88,66,34,43],
}
#print(marks["jim"][4])
ans=dict(sorted(marks.items(),key=lambda x:x[1][4]))
print(ans)


# non uniform dict

marks={
    "jim":[2,44,56,32,33],
    "alex":[44,88,55,65],
    "mark":[65,44],
    "jade":[67,88,66,34,43],
}

ans=dict(sorted(marks.items(),key=lambda x:x[1][-1]))
total_marks=dict(sorted(marks.items(), key=lambda x: sum(x[1]),reverse=True))
print(ans)
print(total_marks)




students={
    "jim":{"maths":44,"eng":66,"science":47},
    "alex":{"maths":50,"eng":34,"science":88},
    "tom":{"maths":60,"eng":70,"science":75}
}

#ans=dict(sorted(students.items(),key=lambda x : x[1]["maths"],reverse=True ))
ans=dict(sorted(students.items(),key=lambda x : sum(x[1].values()),reverse=True ))
print(ans)

"""
