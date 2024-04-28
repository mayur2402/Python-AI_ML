import sys;

print("Recurssion limit is ", sys.getrecursionlimit())

sys.setrecursionlimit(1500)

print("Recurssion limit is ", sys.getrecursionlimit())