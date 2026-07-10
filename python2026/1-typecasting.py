
# int("100abc") throw error
#int("100.4") throw error it work with float casting

num1= float("100.5")
num2=int("200")

print(num1+num2)

print(num1,type(num1))
print(num2,type(num2))

#unsupported operand
#print(100+"100")
#
#  it work it will multiply 100 with a
print(100*"a")