print("Demonstration of Set")

# Data : Heterogeneous
# Ordered : No
# Indexed : No
# Mutable : Yes
# Duplicates : No

data = {11,21,51,101,21,11}
data1 = {11,90.80, True, "Hello"}       #Heterogeneous

print("First set data", data)
print("Lenght of data",len(data))
print("Data at Heterogeneous ", data1)
print("Data at Not ordered ", data1)
# print("Data at index 2", data1[2])
# print("Data with Duplicates elements", data)

print("Set is mutable")
#Insert elemnt in set
data.add(211)
print("Data after insertion:",data)

#remove element
data.remove(211)
print("Data after removal:",data)

data.remove(201)            #show KeyError = 201
print("Data after removal:",data)

data.discard(201)           #if value is there it will remove but does not show error
print("Data after discard:",data)
