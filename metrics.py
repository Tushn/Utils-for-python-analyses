# ----------------------------------------------------
# ----------------  Metrics  -------------------------
# ----------------------------------------------------

def penrose(matrix):
    tam = matrix[0].shape[1];
    result = np.zeros([len(matrix), len(matrix)]);
    #np.cov(matrix.transpose())
    covs = [];
    means = [];
    for i in range(len(matrix)):
        covs.append(np.cov(matrix[i].transpose()));
        means.append(matrix[i].mean(axis=0));
    covs = np.array(covs)
    V = covs.mean(axis=0)
    
    for i in range(0,len(matrix)-1):
        for j in range(i+1,len(matrix)):
            for k in range(tam):
                result[i][j] += pow(means[i][k]-means[j][k], 2)/(tam*V[k][k])
    return result;



def mahalanobis(matrix):
    result = np.zeros([len(matrix), len(matrix)]);
    #np.cov(matrix.transpose())
    covs = [];
    means = [];
    for i in range(len(matrix)):
        covs.append(np.cov(matrix[i].transpose()));
        means.append(matrix[i].mean(axis=0));
    covs = np.array(covs)
    C = np.linalg.inv(covs.mean(axis=0));
    
    for i in range(0,len(matrix)-1):
        for j in range(i+1,len(matrix)):
            result[i][j] = np.dot(np.dot(np.matrix(C),(means[i]-means[j])), (means[i]-means[j]));
    return result;


# Max value in matrix made list of list
# bug fix, lists can be tensor
def maxList(ls):
    maxValue = ls[0][0];
    for row in ls:
        for cell in row:
            if(maxValue < cell):
                maxValue = cell;
    return maxValue;

# Count elements without a pair value
def count_without_pair(vet):
    import numpy as np
    keysHash = list(set(vet));
    
    vet = np.array(vet);
    count = 0;
    for keyH in keysHash:
        if(np.where(vet==keyH)[0].shape[0]==1):
            count += 1;
    return count;
