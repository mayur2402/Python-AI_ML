#List Datatype 

# Heterogeneous
# Ordered
# indexed
# muttable 
# allow duplicate


Arr1 = [10,20,30,40]

print(type(Arr1))

arr2 = [11,78.90,True,"Marvellous",11]

for data in arr2:
    print(data)

print(arr2[3])
print(arr2[0])
arr2[0] = 24
print(arr2[0])
print(id(arr2))
arr2.append(200)
print(id(arr2))
print(arr2)