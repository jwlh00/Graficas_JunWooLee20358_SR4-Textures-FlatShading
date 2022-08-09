import math

def multiply2(matrix1, matrix2):
    matrixtemp = []
    for k in range(len(matrix1)):
        matrixtemp.append([])
        for m in range(len(matrix2)):
            matrixtemp[k].append(mult(getnxt(matrix1, k), getcol(matrix2, m)))
            
    return matrixtemp

def mult(nxt, col):
    try:
        sizenxt = len(nxt)
        sizecol = len(col)
        if (sizenxt != sizecol):
            raise ValueError("Exception")
        res = sum([nxt[k] * col[k] for k in range(sizenxt)])
        return res
    except ValueError:
        print("not same length of row and column")
        
def getcol(matrix, numcol):
    size = len(matrix)
    col = [matrix[k] [numcol] for k in range(size)]
    return col

def getnxt(matrix, numnxt):
    nxt = matrix[numnxt]
    return nxt

def matrixbyvector(vector, matrix_):
    tempvaluesMatrix = []
    matrixtemp = []
    counter = 0
    rowcounter = 0
    
    for row in matrix_:
        if (rowcounter != 0):
            rowcounter += 1
        tempvaluesMatrix.append([])
        if counter == len(vector):
            counter = 0
            if (rowcounter == 0):
                rowcounter += 1
        for value in row:
            tempval = value * vector[counter]
            tempvaluesMatrix[rowcounter].append(tempval)
            counter += 1
            
    for row in tempvaluesMatrix:
        sumOf = sum(row)
        matrixtemp.append(sumOf)
        
    return matrixtemp

def array(arr):
    arrays = []
    for i in arr:
        arrays.append(i)
    return arrays

def negativeArray(arr):
    arrays = []
    for i in arr:
        val = -i
        arrays.append(val)
    return arrays

def dot_twoVectorsOfSameSize(vec1, vec2):
    arrays = []
    for i in range(len(vec1)):
        val = vec1[i] * vec2[i]
        arrays.append(val)
        
    return sum(arrays)

def subtract_twoVectorsOfSameSize(vec1, vec2):
    arrays = []
    for i in range(len(vec1)):
        val = vec1[i] - vec2[i]
        arrays.append(val)
    return arrays

def cross_twoVectorsOfOneByThree(vec1, vec2):
    arrays = []
        
    val = (vec1[1] * vec2[2]) - (vec1[2] * vec2[1])
    arrays.append(val)
    val = -((vec1[0] * vec2[2]) - (vec1[2] * vec2[0]))
    arrays.append(val)
    val = (vec1[0] * vec2[1]) - (vec1[1] * vec2[0])
    arrays.append(val)
    
    return arrays

def norm(vec):
    array = []
    for i in vec:
        array.append(i*i)
    return math.sqrt(sum(array))
    

def vectorDivideByNumber(vec, num):
    array = []
    for i in vec:
        array.append(float(i/num))
        
    return array
    
   
        
    
        
            
    
    
    
    
    
    
    
    
    
    