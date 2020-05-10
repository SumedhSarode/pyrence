
print("Eat Samosa")
num = int (input("Enter  the  number"))
n=num
for i in range(1,300):
    d1=n%10
    n=n//10
    d2=n%10
    n=n//10
    if d1*d1*d1 +d2*d2*d2+n*n*n==num:
        print(num)
