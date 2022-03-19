from functools import reduce


def createMatrix():
    temp=0
    arr=[]
    size=input("Enter the size of the matrix ")
    for i in range (int(size)):
        temparr=[]
        for j in range (int(size)):
            temp=int(input())
            temparr.append(temp)
        arr.append(temparr)
    return arr

def identityMatrix(size):
    flag_matrix=[]
    for i in range(size):
        temp_matrix = []
        for j in range(size):
            if i==j:
                temp_matrix.append(1)
            if i!=j:
                temp_matrix.append(0)
        flag_matrix.append(temp_matrix)
    return flag_matrix


def multiMatrix(matrix1,matrix2):
    if len(matrix1[0]) != len(matrix2[0]) or len(matrix1) != len(matrix2):
        raise Exception("cant mult 2 matrix with different size ")
    flag_matrix=[([0] * len(matrix2[0])) for i in range(len(matrix1))]
    # iterate through the first matrix rows
    for row in range(0, len(matrix1)):
        # iterate through the second matrix columns
        for col in range(0, len(matrix2[0])):
            # iterate through the second matrix rows
            for row2 in range(0, len(matrix2)):
                flag_matrix[row][col] += mat1[row][row2] * mat2[row2][col]
    return flag_matrix

def printMatrix(matrix):
    for i in matrix:
        print(i)

def det(matrix):
    order=len(matrix)
    posdet=0
    for i in range(order):
        posdet+=reduce((lambda x, y: x * y), [matrix[(i+j)%order][j] for j in range(order)])
    negdet=0
    for i in range(order):
        negdet+=reduce((lambda x, y: x * y), [matrix[(order-i-j)%order][j] for j in range(order)])
    return posdet-negdet



mat1 = [[1, 0, 0],
        [-2, 1, 0],
        [0, 0, 1]]

b = [[4], [6],[8]]

mat2 = [[1, -1, -2],
        [2, -3, -5],
        [-1, 3, 5]]

mat3 = [[0, 2, -1],
        [3, -2, 1],
        [3, 2, -1]]

mat4 = [[0, 2, -1],
        [3, -2, 1],
        [3, 2, 1]]



print(det(mat3))
'''''
arr=identityMatrix(2)

printMatrix(arr)
'''''
