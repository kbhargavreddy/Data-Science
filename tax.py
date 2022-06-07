""" Calculate the tax be paid by employee by taking his annual income,hra,deductions as input rate of tax as follows:
    <300000---no tax
    300000 to 600000 --- 10%
    600000 to 1000000 --- 15%
    >1000000 --- 20% 
"""

an=int(input("enter annual salary"))
hra=12*int(input("enter hra per month"))
other=int(input("enter the other expenses"))
if(other>80000):
    other=80000
total=an-hra-other
if(total<300000):
    print("No tax")
elif(300000<=total<=600000):
    total=total-300000
    print(0.1*total)
elif(600000<=total<=1000000):
    total=total-300000
    print(0.15*total)
else:
    total=total-300000
    print(0.2*total)
