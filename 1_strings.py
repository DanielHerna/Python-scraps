
'''------------------------ types of variables ------------------------'''
# Strings

greeting = "hello there"
awfull_text = "     Ohh LoT Of Spaces        "

low = greeting.lower()
caps = greeting.upper()
proper = greeting.title()
fixed_text = awfull_text.strip().title()

print(low +"\n"+caps+"\n"+proper+"\n"+fixed_text)
print(proper + " " + fixed_text)

print(type(low))

## Slicing characters 
print(low[0]*10)
print(low[-1])
print(low[1:])
print(low[:-6])
