# -*- coding: utf-8 -*-
import copy
def get_filtration(K0,sigma):
    i = 1
    fi = [{} for x in range(len(sigma)+1)]
    fi[0]=K0
    for ind in sigma:
        tmp = copy.deepcopy(fi[i-1])
        sig = sigma[ind]
        if len(sig)<2:
            tmp[0][i]=sig
        else:
            if len(sig)<3:
                tmp[1][i]=sig
            else:
                if len(sig)<4:
                    tmp[2][i]=sig
        fi[i]=tmp
        i+=1
    return fi
    
def bd(sigma):
    tmp = [[] for x in range(len(sigma))]
    for i in range(len(sigma)):
        tmp[i] = [x for x in sigma if x!=sigma[i]]
    return tmp
def isequal(s1,s2):
    return sorted(s1)==sorted(s2)
def key_dist(sigma,val):
    for i in sigma:
        if sigma[i]==val:
            return i
            
def youngest(sigma,sigmas):
    yon = sigmas[0]
    tmp = key_dist(sigma,yon)
    for sig in sigmas:
        if key_dist(sigma,sig)>tmp:
            yon = sig
            tmp = key_dist(sigma,yon)
    return yon

          
def Pair(sigma,sig):
    c = bd(sig)
    if len(c) == 1:
        return -1
    else:
        d = youngest(sigma,c)
         
        
#data structure
K0 = {0:{0:[0]},1:{},2:{}}

#sub question how to generate the sigma
sigma = {0:[0],1:[1],2:[2],3:[3],4:[0,2],5:[0,1],6:[2,3],7:[1,3],8:[1,2],9:[1,2,3],10:[0,1,2]}
#to do list
#sigma = [[1],[2],[3],[[0,2],[0,1]],[2,3],[1,3],[1,2],[1,2,3],[0,1,2]]
#which means [[0,2],[0,1]] born at the same time
fi = get_filtration(K0,sigma)


