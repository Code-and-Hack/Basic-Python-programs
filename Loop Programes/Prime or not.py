

no=int(input("Enter a number: "))



'''
for x in range(2,no):
    if no%x==0:
        print("The number is not prime")
        break
else:
    print("Number is prime")

'''

x=2
while x<no:
    if no%x==0:
        print("The number is not prime")
        break
    x+=1
else:
    print("The number is prime")

