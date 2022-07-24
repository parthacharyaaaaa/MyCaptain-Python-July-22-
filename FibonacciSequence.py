x=0
y=1

n = int(input("Please enter number of elements "))

if n<=0:
    print("Number of elements must be a natural number")
elif n==1:
        print(x)
else:
      print(x)
      print(y)
      for i in range(0,n):
        z=x+y
        x=y
        y=z
        print (z)

          