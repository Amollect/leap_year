#Check year is leap or not

year=int(input("enter the year:"))
if year % 4 == 0:
    if year % 400==0:
        print(year," is leap year and century year ")
    else:
        print(year," is non century year ")
else:
     print(year," is not leap year ")