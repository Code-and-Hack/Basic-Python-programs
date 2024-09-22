

no=int(input("Enter the factorial you want to find: "))
no1=no
f=1

for x in range(1,no+1):
    f=f*x
print("The factorial of the number",no,"is",f)
