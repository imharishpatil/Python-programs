import cmath as m
a=int(input("enter value for a = "))
b=int(input("enter value for b = "))
c=int(input("enter value for c = "))
d=b*b-4*a*c
if d>0:
    root1=-b+m.sqrt(d)/2*a
    root2=-b-m.sqrt(d)/2*a
    print(f"roots are real /n root1={root1} root2={root2}")
elif d==0:
    root1=root2=-b/2*a
    print(f"roots are equal /n root1={root1} root2={root2}")
else:
    root1=-b/2*a+m.sqrt(d)/2*a
    root2=-b/2*a-m.sqrt(d)/2*a
    print(f"roots are imaginary /n root1={root1} root2={root2}")