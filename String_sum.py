def lower_char_value(input_ch):
    if (ord('a') <= ord(input_ch) <= ord('z')):  # Adding the number corresponding to the alphabet
        return (ord(input_ch)-ord('a')+1)


def opration_digit(input_str, int_list):
    if (input_str != "" and int_list != []):
        if (input_str[0] == "*"):
            ans = 1
            for i in int_list:
                ans = ans*i
            return ans
        else:
            ans = 0
            for i in int_list:
                ans = ans+i
            return ans


def str_opration(input_str):
    digit_str = ''
    int_list = []
    negative_exception = 'Negatives not allowed : '
    negative_digit = False
    for i in input_str:
        if i.isdigit():
            digit_str = digit_str + i
        else:
            if digit_str.isdigit():  # checking for digit
                if (negative_digit == True):
                    negative_exception = negative_exception+"-"+digit_str + \
                        " "  # Adding number in string for exception
                    negative_digit = False
                elif (int(digit_str) < 1000):
                    int_list.append(int(digit_str))  # Adding sum
                digit_str = ''
            if (ord(i) == ord('-')):  # for finding -ve number
                negative_digit = True
            int_list.append(lower_char_value(i)) if (
                lower_char_value(i)) else 0

    if (digit_str != '' and int(digit_str) < 1001):
        if digit_str.isdigit():
            if (negative_digit == True):
                negative_exception = negative_exception+"-"+digit_str
                negative_digit = False
            else:
                int_list.append(int(digit_str))

    if (len(negative_exception) > 24):
        return negative_exception  # exception for -ve number
    elif (opration_digit(input_str, int_list) != None):
        return opration_digit(input_str, int_list)
    else:
        return 0
