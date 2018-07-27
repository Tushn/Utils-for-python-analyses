# ----------------------------------------------------
# ----------------  Files -------------------------
# ----------------------------------------------------

def savematrix(matrix, filename='matrix.csv', mode='w'):
    file = open(filename, mode);
    
    height = len(matrix);
    width = len(matrix[0]);
    
    for i in range(0, height):
        file.write(str(matrix[i][0]));
        for j in range(1, width):
            file.write(', '+str(matrix[i][j]));
        file.write('\n');
    file.close();

# count differents for read CSV or  similar texts
def count_dif(vector, delimiter='; '):
    keyHash = {};
    for row in vector:
        for elem in row.split(delimiter):
            if(elem in keyHash):
                keyHash[elem] += 1;
            else:
                keyHash[elem] = 1;
    return keyHash;
