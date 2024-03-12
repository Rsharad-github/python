# Q8 you need to find out factorial of given number
num = int(input('enter number :')) 
def factorial(num):
     if(num == 0):
          return 1
     return  num * factorial(num-1) 
print('factorial of ',num,'is',factorial(num))