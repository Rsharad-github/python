
# Q16 STAR PATTERN 
# (i)
for i in range (1,5):
     for j in range(i):
          print('*',end=' ')
     print('')
# (ii)
for i in range(5,0,-1):
   for j in range(i,0,-1):
        print('*' , end =' ')
   print('')
# (iii)
n=int(input('enter row:'))
for i in range(n):
     for  j in range(n,-1,-1):
          if  (i>=j):
               print('*',end=' ')
          else:
               print(' ',end='')
     print()
# 
# (iv)
for i in range (1,5):
     for j in range(i):
          print(j+1,end=' ')
     print('')

# (v)

def factorial(num):
     i = num
     if(num == 0):
          return  1
     fact =1
     while(i>0):
          fact *= i 
          i-=1
     return  fact

def  nCr(n,r):
     return int ( factorial(n)/(factorial(r)*factorial(n-r)))

def pascal(limit):
     for i in range(limit):
          for  j in range(limit,-1,-1):
               if(i >=j):
                    print(nCr(i,j),end=' ')
               else:
                    print(" ",end='')
          print()


num = int (input('enter  number:'))
pascal(num)

# (vi)
n=7
counter =0
for i in range (n):
     for j in  range(i+1):
          counter+=1
          print(counter,end=' ')
     print()