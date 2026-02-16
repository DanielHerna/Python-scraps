''' List are organized and mutables, on the other hand, tuples are organized by inmutable'''
matrixA = [[1,2,3],
          [4,5,6],
          [7,8,9]]

matrixB = [[1,0,0],
           [0,1,0],
           [0,0,1]]

print(f"The element 1,1 is {matrixA[0][0]}")

numbers = (1,3,7,11)
print(type(numbers))

chess_board: list[list[str|int]] = [
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    [0  ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0],
    [0  ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0],
    [0  ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0],
    [0  ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
]

'''move the white knight from 7,1 to 5,2'''

chess_board[7][1]=0
chess_board[5][2]="N"

print(chess_board)