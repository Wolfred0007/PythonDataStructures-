def greet(name):

    return f"Hello, {name}!"

# result = greet("Alice")
# result2=greet("Wilfred")
# print(result2)
# print(result)
names=["Wilfred","Onesmus","Alice"]


for k in names:
    print(greet(k),end=" ")