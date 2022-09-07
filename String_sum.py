
def StrSum(str):
    sum=0
    c = ''
    msg='Negatives not allowed : '
    neg=False
    for i in str: 
        if i.isdigit():
            c = c + i
        else:                    
            if c.isdigit():  ##checking for digit 
                if(neg==True):
                    msg=msg+"-"+c+" "## Adding number in string for exception 
                    neg=False
                elif(int(c)<1000):
                    sum=sum+int(c)## Adding sum
                c=''
            if(ord(i)==45):##for finding -ve number
                neg=True
            if(96<ord(i)<123): ## Adding the number corresponding to the alphabet
                sum=sum+(ord(i)-96)
    if(c!='' and int(c)<1001):
        if c.isdigit():
            if(neg==True):
                msg=msg+"-"+c
                neg=False
            else:
                sum=sum+int(c)
              
    if(len(msg)>24):
        return msg ##exception for -ve number 
    else:
        return sum