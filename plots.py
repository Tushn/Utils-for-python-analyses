#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 11:28:55 2018

@author: root
"""

# -------------------------------------------------------------
# ------------------  Barplots  ------------------------------
# -------------------------------------------------------------
# Barplot plot a bar of vector, it is count data and make labels

# If label is not defined data is generated based values of array
# Else if label is defined they are changed automatically

def barplot(vet, labels='', color='#1f77b4', title='', reverse=True):
    import matplotlib.pyplot as plt
    import numpy as np
    
    listvet = list(set(vet))
    i = 0
    while(i < len(listvet)):
        if(isinstance(listvet[i], (float))):
            del listvet[i]
            break
        i += 1
#    if(isinstance(listvet[0], (float))):
#        keys = sorted(listvet[1:], reverse=reverse)
#    else:
#        keys = sorted(listvet, reverse=reverse)
    keys = sorted(listvet, reverse=reverse)
    counts = np.zeros([len(keys)])
    for key in keys:
        counts[keys.index(key)] = vet.count(key)
    
    if(labels!=''):
        temp = [];
        for key in keys:
            temp.append(labels[key]);
        keys = temp;
    
    plt.barh(np.arange(len(keys)), list(counts), color=color )
    plt.yticks(np.arange(len(keys)), keys)    
    plt.title(title)
    plt.show()
    
    return [keys, counts];
    
# ----------------------------------------------------
# -----------------  Correlation matrix  -------------
# ----------------------------------------------------
def correlation_matrix(df, labels=[], title='', labelx = [], labely = [], save=False, size = 6, scalecolor='default'):
    '''
        correlation_matrix(df, labels=[], title='', labelx = [], labely = [], save=False, size = 6, scalecolor='default')
        
        Inputs:
        ----------------------------
        df : numpy.array
            enter with correlation matrix, you can get a this with:
            >> import numpy as np
            >> df = np.corrcoef(mat)
        labels : list
        title : string
        labelx : list
        labely : list
        save : boolean
        size : integer
        scalecolor : string
            
    '''
    from matplotlib import pyplot as plt
    from matplotlib import cm as cm
    import numpy as np
#    df = (df+1)/2;
#    df = (df - df.min())/(df.max() - df.min())
    
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    if(scalecolor=='default'):
        cmap = cm.get_cmap('jet', 50)
    elif(scalecolor=='gray'):
        cmap = cm.get_cmap('gray')
    else:
        cmap = cm.get_cmap(scalecolor);
#    cax = ax1.imshow(df.corr(), interpolation="nearest", cmap=cmap)
    cax = ax1.imshow(df, interpolation="nearest", cmap=cmap)
    cax.set_clim(-1,1)
    
    ax1.grid(True)
    plt.title(title);
    
    if(len(labels)>0):
        # labels=['Sex','Length','Diam','Height','Whole','Shucked','Viscera','Shell','Rings',]    
        T = np.arange(len(labels))
        ax1.set_yticks(T);
        ax1.set_xticklabels(labels,fontsize=size);
        ax1.set_yticklabels(labels,fontsize=size);
    if(len(labelx)>0):
        T = np.arange(len(labelx))
        ax1.set_xticks(T);
        ax1.set_xticklabels(labelx,fontsize=size);
    if(len(labely)>0):
        T = np.arange(len(labely))
        ax1.set_yticks(T);
        ax1.set_yticklabels(labely,fontsize=size)
    # Add colorbar, make sure to specify tick locations to match desired ticklabels
    tick = [];
    for i in range(0,11):
        tick.append(1-i*0.2)
    
#    for i in range(0,11):
#        tick.append(1-i*0.05)
#    fig.colorbar(cax, ticks=[.75,.8,.85,.90,.95,1])
#    fig.colorbar(cax, ticks=[.75,.8,.85,.90,.95,1])
    fig.colorbar(cax, ticks=tick)
#    fig.clim(-1, 1);
    
    plt.show()
    if(save):
        fig.savefig(title+'.png')
