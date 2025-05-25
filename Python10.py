arr1 = list(map(int, input("Enter array 1: ").split()))
print(arr1)
arr2 = list(map(int, input("Enter array 2 similar to 1: ").split()))
print(arr2)
missing = set(arr1) - set(arr2)
print("Missing element is:",list( missing))

