#CHECK IF A NUMBER BELONGS TO THE FIBBONACCI SEQUENCE.
n=int(input("Enter n value = "))
fib1=0
fib2=1
if fib1==n or fib2==n:
    print(f"{n} belongs to fibbonacci sequence")
else:
    fib3=0
    flag=False
    while fib3<=n:
        fib3=fib1+fib2
        if fib3==n:
            flag=True
            break
        fib1=fib2
        fib2=fib3
if flag==True:
    print(f"{n} belongs to the fibbonacci sequence.")
else:
    print(f"{n} not belongs to the fibbonacci sequence.")