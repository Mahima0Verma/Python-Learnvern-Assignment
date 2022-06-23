#Write a recursive funtion to calculate the sum of number from 0 to 10.
def sum(n):
    if(n==1): #base condition is necessary for perform recursion
        return 1
    else:
        return n+sum(n-1)


n=10
print(sum(n))        

       

