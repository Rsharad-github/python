# Q15 PALINDROME NUMBER(500-1000)
for num in range(505,1000):
   n1 = num
   rev_num = 0
   while num!=0:
        digit = num%10
        rev_num =rev_num*10+digit
        num//=10
   if (n1 == rev_num):
        print(n1,end=' ')