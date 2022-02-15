import time
localtime =time.localtime(time.time()) #it prints time and calender
localtime = time.asctime() #it prints the current local time
print(localtime)
n=int(input("Enter the number: "))
c=0
a=1
b=1
if n==0 or n==1:
    print("Yes")
else:
    while c<n:
        c=a+b
        b=a
        a=c
    if c==n:
        print("Yes")
    else:
        print("No")