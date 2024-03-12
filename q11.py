
# Q11 PALINDROME NUMBER
num =int(input('enter num:'))
n1 =num
rev_num =0
while num!=0:
     digit = num%10
     rev_num =rev_num*10+digit
     num//=10
if (n1 == rev_num):
     print(n1,'is palindrome')
else:
    print(n1,'is not palindrome')