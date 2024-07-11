# define list
list1= ["A","B","C","D","E"]

#print the lsit
print(list1)

#access the elements of lists
print(list1[3])

#total no. of element in the list
print(len(list1))

#replace an element from list
list1[3]="F"
print(list1)

#find the index no. of an element
x=list1.index("C")

#append an element inthe list
list1.append("G")
print(list1)

#insert an element on a specific index no.
list1.insert(2,"H")
print(list1)

#loop with the list
for x in list1: 
    print(x)
    print("Z")         

#check  if the element exists or not
if "A" in list1:
    print("yes, its present")

