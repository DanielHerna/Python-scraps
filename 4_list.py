groceries = ["rice","beans","meat","water","kiwi","apples","beans"]
days = ["Monday","Tuesday","Wednesday","Thrusday","Friday", "Saturday","Sunday"]

groceries.append("bananas")
groceries.insert(0, "protein")
print(f" The index of protein is {groceries.index("protein")}")
print(f"Beans is included {groceries.count("beans")} times")
print(groceries)

groceries.extend(days)
print(groceries)


groceries.remove("beans")
groceries.pop(1)

index_days = groceries.index("Monday")
groceries = groceries[:index_days]

days.clear()
print(groceries)
print(days)

''' INTERESTING, to assign a list to a new variable the operator = is not enough and I will need to use copy 
to allocate a separate space in the memory so changes in list_1 will not be reflected in list_2 
'''

letters = ["A","B","C","D","E"]
letters2 = letters.copy()

letters.remove("B")
print(letters2)

print(id(letters))
print(id(letters2))

