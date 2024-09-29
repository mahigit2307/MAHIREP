import numpy as np
mat=[[i+1 for i in range(7)]for j in range(7)]
arr=np.array(mat)
dim_mat=np.shape(mat)[0]
print("The original matrix is:\n",arr)
n=int(input("Enter the dimension of small metrix:"))
border=n//2
dim_big=dim_mat+(2*border)
mat_big=[[0 for i in range(dim_big)]for j in range(dim_big)]
for i in range(border,dim_big-border):
    for j in range(border,dim_big-border):
        mat_big[i][j]=mat[i-border][j-border]
arr_big=np.array(mat_big)
print("matrix with border is\n",arr_big)
for k in range(0,dim_big-n+1):
    for l in range(0,dim_big-n+1):
        small_mat=[]
        for i in range(l,l+n):
            for j in range(k,k+n):
                small_mat.append(mat_big[i][j])
        small_mat.sort()
        mat[l][k]=small_mat[(n**2)//2]
arr_ans=np.array(mat)
print("the final answer:\n",arr_ans)