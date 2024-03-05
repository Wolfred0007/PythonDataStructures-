name="FreeCodeCamp - Object-Oriented Programming in Python"
vowels=["A","E","I","O","U",]
count=0
for k in name:
    if str(k).upper() in vowels:
        count=count+1
print(name,end="")
print(" contains ",end="")
print(count,end="")
print(" vowels ")
print(f"{name} contains {count} vowels")