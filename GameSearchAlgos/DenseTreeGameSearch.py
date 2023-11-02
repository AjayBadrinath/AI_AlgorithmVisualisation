'''
This is the Updated version and works for any sort of heterogenous game tree
Unlike the previous one the input is considered as the game tree itself.

'''
import numpy as np

MAX=np.inf
MIN=-np.inf

'''
    Creating a Tree Data Structure for unbalanced,Dense,non-uniform-depth tree.
    Class Node just has val,child arr as its components;
'''

class Node:
    def __init__(self,val,children=[]):
        self.val=val
        self.children=children


'''
Normal MiniMax with the node as the change compared to the bottom up approach
'''

def minimax(node,ismaxnode):
    
    if(not node.children):
        return node.val
    
    if(ismaxnode):
        best=MIN
        for i in node.children:
            val=minimax(i,False)
            best=max(best,val)
        return best
    
    else:
        best=MAX
        for i in node.children:
            val=minimax(i,True)
            best=min(val,best)
        return best
    
'''
Same Alpha-Beta Pruning with the node as one of parameter.Recur from top down
'''

def Alpha_Beta_Pruning(node,ismaxnode,alpha,beta):
    
    if(not node.children):
        return node.val
    
    if(ismaxnode):
        best=MIN
        for i in node.children:
            val=Alpha_Beta_Pruning(i,False,alpha,beta)
            best=max(best,val)
            alpha=max(alpha,best)
            if(alpha>=beta):
                print(f"Pruned node{i.val}")
                break
        return best
    
    else:
        best=MAX
        for i in node.children:
            val=Alpha_Beta_Pruning(i,True,alpha,beta)
            best=min(best,val)
            beta=min(beta,best)
            if(alpha>=beta):
                print(f"Pruned node{i.val}")
                break
        return best
    
'''
There is no other way to automate the graph so manual values have to be the input,
I have built the tree for qn 2
Do Feel Free to change the inputs inside the function.. 
Do remember to construct the tree from
bottom-up for keeping track of nodes to avoid confusion

'''
def BuildTree():
    
    x=Node(0.88,[])
    y=Node(-0.98,[])
    p1=Node(np.inf,[x,y])
    x1,x2=Node(-8,[]),Node(-9,[])
    p2=Node(np.inf,[x1,p1,x2])
    x3,x4=Node(0,[]),Node(9,[])
    p3=Node(np.inf,[x3,p2,x4])
    p4=Node(np.inf,[p3])
    y1,y2=Node(-9,[]),Node(-8.9,[])
    t1=Node(np.inf,[y1,y2])
    y3=Node(7,[])
    t2=Node(np.inf,[y3])
    y4=Node(-0.009,[])
    t3=Node(np.inf,[t1,t2,y4])
    y5,y6=Node(78,[]),Node(-7.8,[])
    t4=Node(np.inf,[y5,y6])
    t5=Node(np.inf,[t4])
    y7=Node(4,[])
    t6=Node(np.inf,[y7,t3,t5])
    y8,y9,y10=Node(6,[]),Node(-7,[]),Node(0.8,[])
    t6=Node(np.inf,[y8,y9,y10])
    y11=Node(-0.66,[])
    t7,t8=Node(np.inf,[t6]),Node(np.inf,[y11])
    t9=Node(np.inf,[t7,t8])
    t10=Node(np.inf,[t6,t9])
    z1,z2,z3=Node(67,[]),Node(-6.7,[]),Node(0.067,[])
    s1=Node(np.inf,[z1,z2,z3])
    z4=Node(0.66,[])
    s2=Node(np.inf,[z4,s1])#
    z5,z6=Node(99,[]),Node(9.9,[])
    s3=Node(np.inf,[z5,z6])
    z7=Node(-0.09,[])
    s4=Node(np.inf,[s3,z7])#
    z8,z9=Node(87,[]),Node(8.7,[])
    s4=Node(np.inf,[z8,z9])
    s5=Node(np.inf,[s4])#
    z10=Node(-99,[])#
    s6=Node(np.inf,[s2,s4,s5,z10])
    root=Node(np.inf,[p4,t10,s6])
    return root

#return root

root=BuildTree()

#since we are going from root to leaf so we set ismaxnode =True as the root is the agent that tries to maximize its score

print(Alpha_Beta_Pruning(root,True,MIN,MAX))

print(minimax(root,True))
