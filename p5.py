#program to check a number is prime or not.
n=int(input("Enter n value = "))
i=2
flag=False
while i<=n//2:
    r=n%2
    if r==0:
        flag=True
        break
    i+=1
if flag==True:
    print(f"{n} is not prime number")
else:
    print(f"{n} is prime number")