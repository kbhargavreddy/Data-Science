""" Create a database having employess data """
ans=[]
for i in range(2):
    l=[]
    id1=int(input("enter id"))
    name=input("enter name")
    marks_ssc=int(input("ssc marks"))
    marks_intermediate=int(input("inter marks"))
    cgpa=float(input("btech cgpa"))
    lang=input("preffered language")
    career=input("career choice")
    l.append(id1)
    l.append(name)
    l.append(marks_ssc)
    l.append(marks_intermediate)
    l.append(cgpa)
    l.append(lang)
    l.append(career)
    ans.append(l)
print(ans)


#using dictionary
d=dict()
d[0]={101,'bhargav',980,978,'pyhton','data science'}
d[1]={102,'saatvik',940,928,'pyhton','web tech'}
d[2]={103,'lakshma',1000,1000,'all lang','everything'}
