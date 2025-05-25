str = input("enter the string contain cat and hat  ")

count_cat = str.count("cat")
count_hat = str.count("hat")

if count_cat==count_hat==0:
    print("No cat and hat")
elif count_cat == count_hat:
    print(True)
else:
    print(False)
  
