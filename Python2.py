n = int(input("Enter a natural number n: "))

for i in range(1, n+1):
    sq = 0
    for j in range(1, i+1):  
           sq += j * j
    print(sq)
  
