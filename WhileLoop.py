# define the value 
i =1
while i<10:
    print(i)
    i+=1

# Using break
print()
i = 1
while i<5:
    print(i)
    if i==3:
        break
    i +=1

# Using continue
print()
i = 0
while i<5:
    i +=1
    if i==3:
        continue
    print(i)

# Using else
print()
i = 1
while i<5:
    print(i)
    i +=1
else:
    print("loop executed succefully")

