my_list = [1, 2, 3, 4, 5]
my_dict = {3: "apple", 5: "banana", 7: "cherry"}
K = int(input("Enter the key K: "))

if K in my_list and K in my_dict:
    print("Value from dictionary:", my_dict[K])
else:
    print("K is not present in both list and dictionary.")
  
