#Define a listt

list1= ["A","B","C","D","E"]
list2=["1","2","3","4","5"]

print(list1)

#using remove()
list1.remove("C")
print(list1)

#USing pop() with index number 
list1.pop(1)
print(list1)


#USing pop() without index number 
list1.pop()
print(list1)

print(list2)

# using del keyword with index no.
del list2[3]
print(list2)

#delete whole list
del list2
#print(list2)

#using clear
list1.clear
print(list1)

