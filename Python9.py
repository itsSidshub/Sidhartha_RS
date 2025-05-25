my_list = input("Enter your list")

# Convert list to set
if len(set(my_list)) == len(my_list):
    print("All elements are unique.")
else:
    print("No unique elements.")
  
