def countdigit(n):
    count= 0 
    temp =n
    while temp!=0:
        rem = temp%10
        if rem!= 0 and n%rem== 0 :
            count+=1
        temp= temp//10
    return count   
    
#driver code 
n = 12;
print("the number are : %d" % (countdigit(n)));       