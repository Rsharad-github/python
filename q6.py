#Q6 PRIME/COMPOSITE NUMBER
num = int(input('check whether the number is prime:'))
is_prime = True
for i in range(3,num,2):
     if(num%i == 0):
          is_prime = False
if(is_prime):
     print(num ,'is prime')
else:
     print(num,'is not prime')