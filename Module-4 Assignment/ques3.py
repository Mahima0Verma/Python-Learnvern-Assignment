#Write a function calculation() such that it accept two variable and calculate the addition,subtraction and division.
def calculation(x,y):
    r=x+y
    s=x-y
    t=x/y
    return r,s,t
a=calculation(3,4)
print(a)   