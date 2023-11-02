import math,numpy as np
'''
This Works only for Perfectly Balanced Binary Tree
that satisfies logn(k)-->Int and 
has Only the State Array as input
For an Updated version Use the DenseTreeGameSearch version of the implementation

'''
# Alpha - Beta Pruning
# some upper and lower bounds
MAX=np.inf
MIN=-np.inf
# define game-state array here
arr=[8,7,3,9,9,8,2,4,1,8,8,9,9,9,3,4 ]
# lim Finds the number of levels to recur.
lim=math.log(len(arr),2)

# AB Pruning is a wrapper to the min max algorithm that cuts the search tree by saving compute time..
def Alpha_Beta_Pruning(state_arr,index,depth,ismaxnode,alpha,beta):
    if(depth==lim):
        return state_arr[index]
    if(ismaxnode):
        best=MIN
        for i in range(2):
            val=Alpha_Beta_Pruning(state_arr,index*2+i,depth+1,False,alpha,beta)
            best=max(best,val)
            alpha=max(alpha,best)
            if(alpha>=beta):
                print(f"Pruned at depth :{depth+1}")
                break
        return best
    else:
        best=MAX
        for i in range(2):
            val=Alpha_Beta_Pruning(state_arr,index*2+i,depth+1,True,alpha,beta)
            best=min(best,val)
            beta=min(beta,best)
            if(alpha>=beta):
                print(f"Pruned at depth :{depth+1}")
                break
        return best

'''
Min max
'''    
#Min max is the base algorithm for alpha beta pruning so the code base has less changes .

def minmax(state_arr,index,depth,ismaxnode):
    if(depth==lim):
        return state_arr[index]
    if(ismaxnode):
        best=MIN
        for i in range(2):
            val=minmax(state_arr,index*2+i,depth+1,False)
            best=max(best,val)
        return best
    else:
        best=MAX
        for i in range(2):
            val=minmax(state_arr,index*2+i,depth+1,True)
            best=min(best,val)
        return best

    
print("Alpha Beta Pruning:",Alpha_Beta_Pruning(arr,0,0,True,MIN,MAX))
print("Min-Max Algorithm :",minmax(arr,0,0,True))
