from functools import reduce

def identityMatrix(size):
    """

    makes size*size identity matrix and return it
    :param size: size of the matrix
    :return: the identity matrix
    """
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


def printMultiMatrix(elementary,matrix,result):
    """

    print the elementary matrix multiply the main matrix and the result of them
    :param elementary: elementary matrix
    :param matrix: the matrix
    :param result: the result of the multiplication
    """
    size=len(matrix)
    for i in range (size):
        print(elementary[i],matrix[i]," ",result[i])
    print("\n")

def printMatrix(matrix):
    """

    print matrix
    :param matrix: the matrix
    """
    for i in matrix:
        print(i)
    print("\n")

def printVector(vector):
    """

    print vector
    :param vector: the vector
    """
    for i in vector:
        print("[",i,"]")
    print("\n")

def det(matrix):
    """

    calc the determinant
    :param matrix: the matrix
    :return: the determinant
    """
    order=len(matrix)
    posdet=0
    for i in range(order):
        posdet+=reduce((lambda x, y: x * y), [matrix[(i+j)%order][j] for j in range(order)])
    negdet=0
    for i in range(order):
        negdet+=reduce((lambda x, y: x * y), [matrix[(order-i-j)%order][j] for j in range(order)])
    determinant=posdet-negdet
    return determinant



def elementaryMatrix(matrix,b):
    """

    calculate the elementary matrix, prints every multiplication, and prints the multiplication of all the elementary matrices wich is the inverse matrix
    :param matrix:the matrix
    :param b: the vector B
    :return: the inverse matrix
    """
    size=len(matrix)
    mulOfAllElememtary = identityMatrix(size)
    e=1
    for i in range(size):
        elementary = identityMatrix(size)
        if matrix[i][i]!=1:
            elementary[i][i]=1/matrix[i][i]
            print(f"Iteration {e}:")
            e=e+1
            result=multi(elementary, matrix)
            printMultiMatrix(elementary,matrix,result)
            #print(elementary, matrix, result)
            matrix=result
            mulOfAllElememtary = multi(elementary, mulOfAllElememtary)

        j = 0
        for j in range(size):
            if matrix[j][i]!=0 and j!=i :
                elementary = identityMatrix(size)
                elementary[j][i]=matrix[j][i]*-1 
                print(f"Iteration {e}:")
                e = e + 1
                result = multi(elementary, matrix)
                printMultiMatrix(elementary, matrix, result)
                #print(elementary,matrix,result)
                mulOfAllElememtary = multi(elementary, mulOfAllElememtary)
                matrix=result
    print("the The inverse matrix is: ")
    printMatrix(mulOfAllElememtary)
    return mulOfAllElememtary


def multi(m1,m2):
    """

    multiply two matrix and return the result(the place matters m1*m2 is different m2*m1)
    :param m1: first matrix
    :param m2: second matrix
    :return: result of multiplication
    """

    size=len(m1)
    zeroMat=[]
    line=[]
    for i in range(size):
        zeroMat.append([])
        for j in range(size):
            zeroMat[i].append(0)
    i,j,k=0,0,0
    for i in range(size):
        for j in range(size):
            for k in range(size):
                zeroMat[i][j] += m1[i][k] * m2[k][j]
    result=zeroMat
    return result


def sort(matrix,b):
    """

    sorts every column in the given matrix and vector (from the biggest to the smallest)
    :param matrix:the matrix
    :param b: B
    :return: the sorted matrix
    """
    if (det(matrix)==0):
        print("The determinant of the given matrix is equal to zero and therefore has no inverse matrix ")
        return 0
    if len(matrix[0]) != len(b):
        print("Error! The size of the column in the matrix must be equal to the size of the row in the vector ")
        return 0
    size=len(matrix)
    for col in range(size):
            row=col
            pivot,max=col,col
            for j in range(size-col-1):
                row+=1
                if abs(matrix[row][col])>abs(matrix[pivot][pivot]) and abs(matrix[row][col])>abs(matrix[max][col]):
                    max=row
            if max!=pivot:
                temp=b[pivot]
                temp2 = matrix[pivot]
                b[pivot]=b[max]
                matrix[pivot] = matrix[max]
                b[max]=temp
                matrix[max] = temp2
    return matrix



def multMatrixVector(matrix,vector):

    """
    multiply matrix and vector
    :param matrix: matrix
    :param vector: vector
    :return: result of multiplication
    """
    if len(matrix[0])!=len(vector):
        print("Error")
        return 0
    sol=[]
    for i in range(len(matrix)): #all the row in the matrix
        for j in range(len(matrix)): #all element in the row
            temp=0
            for k in range(len(vector)): ##all the element in the vector
                temp=temp+(matrix[i][k]*vector[k])
        sol.append(temp)
    return sol

def calcMatrix(matrix,b):

    """
    function that gathers all the other functions and print the final result
    :param matrix: the matrix
    :param b: B
    """
    matrix = sort(matrix, b)
    if matrix==0:
        return 0
    print("Sorted matrix:")
    printMatrix(matrix)
    print("Sorted B:")
    printVector(b)
    matrix = elementaryMatrix(matrix, b)
    print("the result is:", multMatrixVector(matrix, b))



matrix = [[3,-2,4],
        [1,0,2],
        [0,1,0]]
b = [11, 7,2]



calcMatrix(matrix,b)

