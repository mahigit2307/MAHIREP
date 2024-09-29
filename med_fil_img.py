import cv2
import numpy as np

# inputting filename and filetype
#filename=input("enter the filename:")
#filetype=input("enter the filetype:")
file_address="mahi_pic_art_noisy.jpg"
# reading image containing noise into a matrix
arr=cv2.imread(file_address)
# displaying the image containing noise
cv2.imshow('noisy image',arr)
cv2.waitKey(0)
dim_mat=np.shape(arr)[0]
print(np.shape(arr))

# converting the rgb image into gray image
mat = cv2.cvtColor(arr, cv2.COLOR_BGR2GRAY)
print(np.shape(mat))
mat_dim=np.shape(mat)[0]

# inputting the dimension of the smaller matrix
n=int(input("Enter the dimension of small matrix:"))
border=n//2
dim_big=dim_mat+(2*border)

# adding border to the matrix
mat_big=[[0 for i in range(dim_big)]for j in range(dim_big)]
for i in range(border,dim_big-border):
    for j in range(border,dim_big-border):
        mat_big[i][j]=mat[i-border][j-border]

# median filter process:
for k in range(0,dim_big-n+1):
    for l in range(0,dim_big-n+1):
        # extracting a smaller matrix into a 1D matrix
        small_mat=[]
        for i in range(l,l+n):
            for j in range(k,k+n):
                small_mat.append(mat_big[i][j])
        # sorting its elements to find median
        small_mat.sort()
        # replacing the corresponding pixel with the median(centre element)
        mat[l][k]=small_mat[(n**2)//2]

# displaying the final filtered image
arr_ans=np.array(mat)
op_filename="smooth_image.jpg"
cv2.imwrite(op_filename,arr_ans)
cv2.imshow('median filtered image',arr_ans)
cv2.waitKey(0)