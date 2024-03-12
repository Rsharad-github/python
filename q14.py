
# Q14 ARMSTRONG NUMBER
num =int(input('enter num:'))
n1=number = num 
n =0
while(n1/10 != 0):
     n+=1
     n1 //= 10
# print (n)
arm_num=0
if(n==1):
     print('armstrong number of ',number,'is:',arm_num)
else:
     while(num/10 !=0):
          arm_num += (num%10)**n
          num//=10
     print('armstrong number of ',number,'is:',arm_num)