n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))
print("The prime numbers between these 2 numbers are", end=" ")


#for loop <--
for x in range(n1,n2+1):
    if n1>1:
        for y in range(2,x):
            if x%y==0:
                break
        else:
            print(x, end=", ")




#While loop <--
'''
while n1<=n2:
    x=2
    while x<n1:
        if n1%x==0:
            break
        x+=1
    else:
        print(x, end=", ")
    n1+=1

'''
print("and that's it.")