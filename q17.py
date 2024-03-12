
# Q17 
# (i)
def isPalindrome(num):
    n1 =num
    rev_num =0
    while num!=0:
         digit = num%10
         rev_num =rev_num*10+digit
         num//=10
    if (n1 == rev_num):
         return 1
    else:
        return 0 
# (ii)
def SumOfNaturalNum(num):
   sum = 0
   for i in range (num+1):
        sum += i;
   return sum