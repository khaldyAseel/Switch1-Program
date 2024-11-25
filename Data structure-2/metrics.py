def continuous_nums(arr):
    pointer1 = 0
    pointer2 = 1

    while pointer2 < len(arr):
        # Check if the numbers are consecutive
        if abs(arr[pointer1] - arr[pointer2]) == 1:
            return True
        else:
            pointer1 += 1
            pointer2 += 1  # Move both pointers forward

    return False  # No consecutive numbers found

print(continuous_nums([2,3,5,7]))

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

#print all values col by col 
num_cols = len(matrix[0]) 
num_rows = len(matrix) 

for col in range(num_cols):  # Loop through each column index
    for row in range(num_rows):  # Loop through each row
        print(matrix[row][col])  # Print cell value

matrix1 = [
    [1,2,3],
    [2,4,5],
    [3,5,6]
] #true 

matrix2 = [
    [1,0,-1],
    [0,4,5],
    [-2,5,6]
] #flase 

#find if 2d square matrix is symmetrical on main diagonal
def is_symmetrical(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

print(is_symmetrical(matrix1))
print(is_symmetrical(matrix2))


matrix3 = [
    [2,7,6],
    [9,5,1],
    [4,3,8]
] 

# func gets matrix - checks if magic square - true else - flase 
def magic_square(matrix):
  for i in range(len(matrix)):
    if sum(matrix[i]) != sum(matrix[0]):
      return False
    col_sum = 0
    for j in range(len(matrix)):
      col_sum += matrix[j][i]
    if col_sum != sum(matrix[0]):
      return False
  return True

print(magic_square(matrix3))