# -*- coding: utf-8 -*-
import copy
def bd(sigma):
    tmp = [[] for x in range(len(sigma))]
    for i in range(len(sigma)):
        tmp[i] = [x for x in sigma if x!=sigma[i]]
    return tmp
    
def key_dist(sigma,val):
    for i in sigma:
        if val in sigma[i]:
            return i
    else:
        return val[0]
def ind_dist(sigma,val):
    for i in sigma:
        if val == sigma[i]:
            return i
def youngest(sigma,sigmas,od):
    yon = sigmas[0]
    tmp = key_dist(sigma,[ind_dist(od,yon)])
    for sig in sigmas:
        if key_dist(sigma,[ind_dist(od,sig)])>tmp:
            yon = sig
            tmp = key_dist(sigma,yon)
    return [ind_dist(od,yon)]
    
def paired(sigma,val,i):
    while i>=0:
        if val in sigma[i]:
            return i
        i-=1
    return 0
    
def posK(K):
    pK={}
    for x in K:
        pK[x]=K[x][0]
    return pK
def add(c1,c2):
    for c in c1:
        if c in c2:
            c2.remove(c)
        else:
            c2.append(c)
    return c2
def Pair(sigma):
    K={x:[[],[]] for x in range(len(sigma))}
    pK={x:[[]] for x in range(len(sigma))}
    for i in sigma:
#        print(i)
        sig = sigma[i]
        c = bd(sig)
        if len(c) == 1:
            K[i] = [[i],'unpaired']
            pK={x:[K[x][0]] for x in K}
        else:
            d = youngest(pK,c,sigma)
            index_d = paired(pK,d,i)
            ii = copy.deepcopy(i)
            while K[index_d][1]!='unpaired' and len(c)>0:
#                print(bd(sigma[K[index_d][1][0]]),c)
                c = add(bd(sigma[K[index_d][1][0]]),c)
                if len(c)>0:
                    d = youngest(pK,c,sigma)
                    index_d = paired(pK,d,ii)
                    ii-=1
            if len(c)>1:
#                print('************',youngest(pK,c,sigma))
                K[i] = [d,[i]]
                pK={x:[K[x][0]] for x in K}
            else:
                K[i] = [[i],'unpaired']
                pK={x:[K[x][0]] for x in K}
    return K
            



K={x:[[],[]] for x in range(11)}
sigma = {0:[0],1:[1],2:[2],3:[3],4:[0,2],5:[0,1],6:[2,3],7:[1,3],8:[1,2],9:[1,2,3],10:[0,1,2]}
pK = Pair(sigma)