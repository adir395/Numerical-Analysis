from functools import reduce

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


def printMatrix(matrix):
    for i in matrix:
        print(i)
    print("\n")

def det(matrix):
    order=len(matrix)
    posdet=0
    for i in range(order):
        posdet+=reduce((lambda x, y: x * y), [matrix[(i+j)%order][j] for j in range(order)])
    negdet=0
    for i in range(order):
        negdet+=reduce((lambda x, y: x * y), [matrix[(order-i-j)%order][j] for j in range(order)])
    determinant=posdet-negdet
    if determinant==0:
        print("The determinant of the given matrix is equal to zero and therefore has no inverse matrix ")
    else:
        print(f"the determinant is: {determinant}")

def elementaryMatrix(matrix):
    size=len(matrix)
    mulOfAllElememtary = identityMatrix(size)
    e=1
    for i in range(size):
        elementary = identityMatrix(size)
        if matrix[i][i]!=1:
            elementary[i][i]=1/matrix[i][i]
            print(f"E{e}:")
            e=e+1
            printMatrix(elementary)
            matrix = multi(elementary, matrix)
            printMatrix(matrix)
            mulOfAllElememtary = multi(elementary, mulOfAllElememtary)

        j = 0
        for j in range(size):
            if matrix[j][i]!=0 and j!=i :
                elementary = identityMatrix(size)
                elementary[j][i]=matrix[j][i]*-1 #למה צריך לחלק באיבר המוביל? הוא תמיד 1
                print(f"E{e}:")
                e=e+1
                printMatrix(elementary)
                matrix=multi(elementary, matrix)
                printMatrix(matrix)
                mulOfAllElememtary = multi(elementary, mulOfAllElememtary)
    print("the The inverse matrix is: ")
    printMatrix(mulOfAllElememtary)


def multi(m1,m2):
    size=len(m1)
    zeroMat=[]
    line=[]
    for i in range(size):
        zeroMat.append([])
        for j in range(size):
            zeroMat[i].append(0)
    i,j,k=0,0,0
    # iterate through rows of X
    for i in range(size):
        # iterate through columns of Y
        for j in range(size):
            # iterate through rows of Y
            for k in range(size):
                zeroMat[i][j] += m1[i][k] * m2[k][j]
    result=zeroMat
    return result

#def soloution(reverseMatrix,matB)
 #   {

  #  }


def sort(matrix):
    size=len(matrix)
    for col in range(size):
            row=col
            pivot,max=col,col
            for j in range(size-col-1):
                row+=1
                if abs(matrix[row][col])>abs(matrix[pivot][pivot]):
                    max=row
            if max!=pivot:
                temp=matrix[pivot]
                matrix[pivot]=matrix[max]
                matrix[max]=temp
    print("sort:")
    printMatrix(matrix)
    return matrix



mat1 = [[2,-3, -4],
        [0, 0, -1],
        [1, -2, 1]]

b = [[16], [-8],[0]]

mat2 = [[1, -1, -2],
        [2, -3, -5],
        [-1, 3, 5]]

mat3 = [[1, 0, 2],
        [2, -1, 3],
        [4, 1, 8]]

mat4 = [[1,0,2],
        [2,-1,3],
        [4,1,8]]

det(mat3)

elementaryMatrix(sort(mat3))


#multi([[1, 0, 0], [-2, 1, 0], [0, 0, 1]],[[1, -1, -2], [2, -3, -5], [-1, 3, 5]],3)
#print(multiMatrix([[1, 0, 0], [-2, 1, 0], [0, 0, 1]],[[1, -1, -2], [2, -3, -5], [-1, 3, 5]]))
'''''
arr=identityMatrix(2)
printMatrix(arr)
det(mat2)
sort(mat2)
/elementaryMatrix(mat2)
'''''
