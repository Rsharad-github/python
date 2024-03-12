# Q10 REVERSE NUMBER
num =int(input('enter num:'))
rev_num =0
while (num!=0):
     digit = num%10
     rev_num =rev_num*10+digit
     num//=10
print('rev num',rev_num)