import random
import numpy as np
mat=[[random.randint(0,9) for i in range(5)]for j in range(5)]
arr_mat=np.array(mat)
print("The original matrix is:\n",arr_mat)
mat_big=[[0 for i in range(9)]for j in range(9)]
for i in range(2,7):
    for j in range(2,7):
        mat_big[i][j]=mat[i-2][j-2]
arr_big=np.array(mat_big)
print("matrix with border is\n",arr_big)
for k in range(1,6):
    for l in range(1,6):
        small_mat=[]
        for i in range(l,l+3):
            for j in range(k,k+3):
                small_mat.append(mat_big[i][j])
        small_mat.sort()
        mat[l-1][k-1]=small_mat[4]
arr_ans=np.array(mat)
print("the final answer:\n",arr_ans)
