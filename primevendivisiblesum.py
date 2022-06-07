""" Check the number is prime or not, even or not, divisible by 5 not, sum of digits """
n=int(input())
for i in range(2,int(n**0.5)+1):
    if(n%i==0):
        print("not prime")
        break
else:
    print("prime")
if(n%2==0):
    print("even")
else:
    print("odd")
if(str(n)[-1]=='0' or str(n)[-1]=='5'):
    print("yes")
else:
    print("no")
print("the sum is",(n*(n+1))//2)
