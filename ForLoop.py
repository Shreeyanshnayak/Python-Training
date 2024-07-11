# define a list
list1 = ["1","2","3","4"]
list2 = ["A","B","C","D"]

# For each or for loop
# loop through the list
for x in list1:
    print(x)
    print("I am in inside for loop")

print("I am outside for loop")

# for loop for strings
for x in "PYTHON":
    print(x)

#Nested for loop
for x in list1:
    for y in list2:
        print(x,y)

# using break in for loop
for x in list1:
    print(x)
    if x =="3":
        break

# Using continnue for loop
for x in list1:
    if x =="3":
        continue
    print(x)