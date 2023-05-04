n=int(input("Enter a number"))
while(n>0):
    m=int(n%10)
    n=int(n/10)
    print(m,end="")
