# Q12 FIBONACCI SERIES
num = int(input('enter number :'))
def fib(num):
     if(num<1):
          print('not a valid input')
     if (num==1 or num == 2):
          return num-1
     else:
          return fib(num-1) + fib(num-2)
print (fib(num))