# ----------------------------------------------------
# ------------------  Handfcrafted  ------------------
# ----------------------------------------------------

def count_dif(vector):
    keyHash = {};
    for row in vector:
        for elem in vector:
            if(elem in keyHash):
                keyHash[elem] += 1;
            else:
                keyHash[elem] = 1;
    return keyHash;

def row2vec(vector, keyHash):
    keys = list(keyHash.keys());
    #values = list(keyHash.values());
    
    indices = {};
    i = 0;
    for key in keys:
        if(keyHash[key]>=10):
            indices[key] = i;
            i += 1;

    i = 0;
    keysMat = [];
    for elemts in vector:
        keysMat.append([]);
        for elem in elemts.split('; '):
            if(elem in indices):
                keysMat[i].append(indices[elem]);
        i += 1;
    return [keysMat, indices];

def splitGroups(matrix, group):
    indices = group[0];
    numGroups = len(list(group[1].keys())); # group[1] metadata
    matrices = [];
    
    for i in range(numGroups):
        matrices.append([]);

    for i in range(len(matrix)):
        for indice in indices[i]:
            matrices[indice].append(matrix[i]); 

    for i in range(numGroups):
        matrices[i] = np.array(matrices[i]);
    
    return matrices;

# ainda nao foi testado
def group2matrix(group):    
    #max_group = np.array(group).max()[0];
    max_group = maxList(group);
    #min_group = np.array(groups).min()[0];    
    matrix = np.zeros((len(group) , max_group+1));
    
    for i in range(len(group)):
        if(len(group[i])>0):
            for cell in group[i]:
                matrix[i][cell] = 1;
    
    return matrix;

def matrix2group(matrix):
    group = [];
    for i in range(matrix.shape[0]):
        group.append([]);
        for j in range(matrix.shape[1]):
            if(matrix[i][j] > 0):
                group[i].append(j);
    return group;
