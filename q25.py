# Q25 
# MULTIPLICATION OF MATRIX 
r1 = int(input('no of rows in matrix1 : '))
c1r2 = int(input('no of columns in matrix1 i.e., no of rows in matrix 2  : '))
c2 = int(input('no of columns in matrix 2 : '))
matrix1 =[]
matrix2 = []
result = []
print('enter matrix 1 :')
for i in range(r1):
     a = []
     for j in range(c1r2):
          a.append(int(input()))
     matrix1.append(a)

print('enter matrix 2 :')
for i in range(c1r2):
     a = []
     for j in range(c2):
          a. append(int(input()))

     matrix2.append(a)
for i in range(r1):
     a = []
     for j in range(c2):  
          a.append(0)

     result.append(a)
print(matrix1)
print(matrix2)
for i in range(r1):
     for j in range(c2):
          for k in range(c1r2):
               result[i][j]+=matrix1[i][k]*matrix2[k][j]
print(result)