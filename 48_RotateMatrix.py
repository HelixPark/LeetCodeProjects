matrix=[[5,1,9,11],
        [2,4,8,10],
        [13,3,6,7],
        [15, 14, 12, 16]]

def rotateImage(matrix):
    length=len(matrix)
    for i in range(length//2):
        for j in range(i,length-i-1):
            tmp=matrix[i][j]
            matrix[i][j] = matrix[length - j - 1][i]
            matrix[length - j - 1][i] = matrix[length - i - 1][length - j - 1]
            matrix[length - i - 1][length - j - 1] = matrix[j][length - i - 1]
            matrix[j][length - i - 1] = tmp


# print(matrix)
rotateImage(matrix)
print(matrix)