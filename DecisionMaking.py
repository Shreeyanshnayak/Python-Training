#define values
a=10
b=20
c=30

#if statement
if b>a:
    print("B is grester than A")
    print("I am inside If")
print("I am outside If")

#if - else statement
if b>a:
    print("B is grester than A")
else :
    print("A is greater than B")

#if-else if-else statement
if b>a:
    print("B is grester than A")
elif a==b:
    print("Both are same")
else :
    print("A is greater than B")

#Applicable for only single statement

#Shorthand if
if b>a: print("B is greater than A")

#Shorthand if - else
print("B is grester than A")if b>a else print("A is greater than B")

#Shorthanf if - elif - else
print("B is grester than A")if b>a else print("Both are same") if a==b else print("A is greater than B")

#Using and keyword
if b>a and c>a:
    print("Both B and C are greater than A")

#using or keyword
if b>a or c>a:
    print("Both B and C maybe greater than A")