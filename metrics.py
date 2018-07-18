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
