def armstrongNumber (n):
    n = str(n)
    j = 0
    for i in n:
        j += int(i)**3
    if j == int(n):
        return "Yes"
    else :
        return "No"
       
a=armstrongNumber(153)
print(a)