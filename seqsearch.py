#program for sequencial or linear search
n=int(input("Enter n value = "))
x=[]
for i in range(0,n):
    v=int(input(f"Enter {i} value = "))
    x.append(v)
key=int(input("Enter the number to searched = "))
pos=-1
for i in range(0,n):
    if x[i]==key:
        pos=i
        break
    i+=1
if pos==-1:
    print(f"{key} item is not in the list")
else:
    print(f"{key} item is found at {pos} position")