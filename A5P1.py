
n=int(input("please enter the size (or number) of Pascal/Khayyam triangle: "))
n=n-1
import numpy

A=numpy.zeros([n,n])


for j in range(n):
    for i in range(n):
        if j==i==0:
            A[i][j]=1
        
        elif j>0 and i==0:
            A[j][i]=A[j-1][i]
        elif i>0 and j>0 and j>=i:
         A[j][i]=A[j-1][i]+A[j-1][i-1]






print(A)


   