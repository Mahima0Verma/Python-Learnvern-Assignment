# WAP to find out the grade of given percentage value and print the message according given criteria:
p=float(input("Enter your percentage: "))
if p>=70:
    print("A grade")
elif (p>65 and p<70):
    print("B+ grade")
elif p>60 and p<65:
    print("B grade")
elif p>55 and p<60:
    print("C grade")
elif p<55:
    print("fail")        


