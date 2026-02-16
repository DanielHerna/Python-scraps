from typing import cast

squares = [ x**2 for x in range(11)]

# F = (9/5 *C) + 32
celsius = list(range(10,50,10))

fahrenheit = [(temp*9/5)+32 for temp in celsius]
print(fahrenheit)

even_numbers = [i for i in range(1,11) if i%2==0]
print(even_numbers)


matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

t_matrix = [[0,0,0],[0,0,0],[0,0,0]]

for rows in range(len(matrix[0])):
    for cols in range(len(matrix[0])):
        t_matrix[rows][cols] = matrix[cols][rows]

#print(t_matrix)

#Option 2:

t_matrix_py = []

for i in range(len(matrix)):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    t_matrix_py.append(transposed_row)

print(t_matrix_py)

# comprehension lists 

transposed_m = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transposed_m)

# ---------------------- extra exercises ----------------------

#1

double_numbers = [i*2 for i in range(1,6)]
print(double_numbers)

#2

WORDS=["sol", "mar", "montaña", "rio", "estrella"]

cap_words = [word.upper() for word in WORDS if len(word)>3] 
print(cap_words)

#3

KEYS = ["nombre", "edad", "ocupación"]
VALUES = ["Juan", 30, "Ingeniero"]

members = {KEYS[i]:VALUES[i] for i in range(len(KEYS))}
print(members)

#4

t_matrix_4 = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(t_matrix)

#5
contacts = [
    {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"},
    {"nombre": "Ana", "edad": 32, "ciudad": "Madrid"},
    {"nombre": "Pedro", "edad": 35, "ciudad": "Barcelona"},
    {"nombre": "Laura", "edad": 40, "ciudad": "Madrid"}
]

seniors_spain = [contact for contact in contacts if cast(int,contact["edad"])>30 and contact["ciudad"]=="Madrid"]
print(seniors_spain)

#6 

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
eve_twice = [number*2 if number%2==0 else number for number in numbers]
print(eve_twice)