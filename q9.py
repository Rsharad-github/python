# Q9 sum of digits of a given n digit number
num = int(input('enter number :'))
n1 =num 
sum = 0
while(n1>0):
     sum += n1%10
     n1 = n1//10
print(sum)
