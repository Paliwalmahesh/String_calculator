def lower_char_value(ch):
    if (ord('a') <= ord(ch) <= ord('z')):  # Adding the number corresponding to the alphabet
        return (ord(ch)-ord('a')+1)


def opration_digit(s, li):
    if (s != "" and li != []):
        if (s[0] == "*"):
            ans = 1
            for i in li:
                ans = ans*i
            return ans
        else:
            ans = 0
            for i in li:
                ans = ans+i
            return ans


def str_opration(s):
    c = ''
    li = []
    msg = 'Negatives not allowed : '
    neg = False
    for i in s:
        if i.isdigit():
            c = c + i
        else:
            if c.isdigit():  # checking for digit
                if (neg == True):
                    msg = msg+"-"+c+" "  # Adding number in string for exception
                    neg = False
                elif (int(c) < 1000):
                    li.append(int(c))  # Adding sum
                c = ''
            if (ord(i) == ord('-')):  # for finding -ve number
                neg = True
            li.append(lower_char_value(i)) if (lower_char_value(i)) else 0

    if (c != '' and int(c) < 1001):
        if c.isdigit():
            if (neg == True):
                msg = msg+"-"+c
                neg = False
            else:
                li.append(int(c))

    if (len(msg) > 24):
        return msg  # exception for -ve number
    elif (opration_digit(s, li) != None):
        return opration_digit(s, li)
    else:
        return 0
