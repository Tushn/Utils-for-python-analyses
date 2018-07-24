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
