
#Q18
#(a)DECIMAL TO BINARY

def DecToBin(num): 
     if (num == 0):
          return 0
     else:
          return (num %2 + 10*DecToBin(int(num//2)))
print(DecToBin(7))
# (b)DECIMAL TO OCTEL
def DecToOctel(num): 
     if (num == 0):
          return 0
     else:
          return (num %8 + 10*DecToOctel(int(num//8)))
print(DecToOctel(13))
# (c)FACTORIAL OF NUM
def factorial(num):
     
     if(num == 0):
          return  1
     return  num*factorial(num-1)
# (d)FIBONACCI UPTO NUM
def Fibo(num):
   if(num == 1 or num == 2):
        return num-1
   return Fibo(num-1)+Fibo(num-2)
print(Fibo(5))
