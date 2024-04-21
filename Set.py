#Tupple Datatype 

# Heterogeneous
# UnOrdered
# Unindexed
# muttable 
# duplicate not allowed


arr = {11,22,33,44}

print(type(arr))

print(arr)

arr = {11,22,33,44,"Hello"}

print(arr)

arr = {11,22,33,44,"Hello",11}

print(arr)

arr.add(10)

print(arr)
#print(arr[0])

arr.discard("Hello")

print(arr)

arr.discard(11)

print(arr)