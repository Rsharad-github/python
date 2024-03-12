
# Q23
# TRANSPOSE 
mat1=[[1,5,4],[5,8,2],[8,6,2]]
result=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    for j in range(3):
      result[i][j]=mat1[j][i]
print(result)