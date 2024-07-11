'''
type casting : forceful conversation of one data type into another
'''

a,b,c=1,2.5,'3'
print(a)
print(b)
print(c)

d=int(c) #convert string into int
print(d) 
e=a+d
print(e)
f=int(b) #convert float value to integer
print(f)

g=float(a) #convert to float
print(g)

h=str(a) 
i=c+h
print(i)