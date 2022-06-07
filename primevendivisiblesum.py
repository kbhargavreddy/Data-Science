""" Check the number is prime or not, even or not, divisible by 5 not, sum of digits """

n=int(input("Enter a number"))
if(n%5==0):
  print("It is divisible by 5")
else:
  print("Not divisible by 5")
if(n%2==0):
  print("It is even")
else:
  print("It is odd")
for i in range(2,int(n**0.5)+1):
  if(n%i==0):
    print("It is not a prime")
    break
else:
  print("It is a prime")
sum=(n*(n+1))/2
print(sum)