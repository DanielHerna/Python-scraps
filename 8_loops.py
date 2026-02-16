for i in range(1,11):
    if i==5:
        continue
    
    if i%2==0:
        print(f"The number {i} is even")
    else:
        print(f"The number {i} is odd")

x = 0

while x<=10:
    
    if x==2:
        print("Limit time reached")
        break

    else: 
        print(f"iteration number {x}")
    x += 1


characters = "this is an example"

for char in characters:
    print(char)
    

