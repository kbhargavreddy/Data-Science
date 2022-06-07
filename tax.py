""" Calculate the tax be paid by employee by taking his annual income,hra,deductions as input rate of tax as follows:
    <300000---no tax
    300000 to 600000 --- 10%
    600000 to 1000000 --- 15%
    >1000000 --- 20% 
"""

ai=int(input("Enter annual income"))
hra=int(input("Enter house rent allowences"))
deductions=int(input("Enter other deductions less than 80000"))
taxableincome=ai-(hra*12)-deductions
ta=taxableincome-300000
if(ta<=300000):
  print("No tax")
elif(300000<ta<=600000):
  print(0.1*ta)
elif(600000<ta<=1000000):
  print(0.15*ta)
else:
  print(0.20*ta)