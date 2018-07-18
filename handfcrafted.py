# ----------------------------------------------------
# ------------------  Handfcrafted  ------------------
# ----------------------------------------------------

def count_dif(vector):
    keyHash = {};
    for row in vector:
        for elem in row.split('; '):
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
