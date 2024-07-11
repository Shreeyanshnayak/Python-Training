#define a tuple
tuple1 = ("A","B","C","D","E")
print(tuple1)

#Access the element using index number
print(tuple1[3])

#Check the number of elements in the tuple 
print(len(tuple1))

#return the no. of item specific element is in the tuple
print(tuple1.count("A"))

#Return the index no. of given element
print(tuple1.index("E"))

#loop with tuple
for x in tuple1:
    print(x)

#check if item exist
if "B" in tuple1:
    print("yes its present")

#another way to create a tuple, tuple( constructor)
tuple2 = tuple(("A","B","C","D"))
print(tuple2)