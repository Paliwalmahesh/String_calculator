
def StrSum(str):
    c=''
    sum=0
    for i in str: 
        if i.isdigit():
            c = c + i
        else:                   
            if c.isdigit():
                sum=sum+int(c)
                c=''
    if(c!=''):
        if c.isdigit():
            sum=sum+int(c)
    return(sum)