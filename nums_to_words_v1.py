#!/usr/bin/python3
import re
import inflect


equation = input("Enter the equation: ")

def solve(s):
    p = inflect.engine()
    nums = '01234567890'
    signs = '+-*/= '
    allowed_chars = nums + signs
    verbose_signs = {'+': 'plus', '-': 'minus', '*': 'multiple by', '/': 'divide by', '=': 'equals'}
    
    if any(i not in allowed_chars for i in equation):
        return "invalid input"
    if '=' not in s and not any(i in '+-*/' for i in s):
        return "invalid input"

    s = s.strip()


    s = ''.join(s.split())
    # s = s.lstrip('+')
    # s = s.lstrip('-')

    result = ''

    tmp = ''
    for i, v in enumerate(s):
        if v in nums:
            tmp += v
            if i == len(s) - 1:
            	result += p.number_to_words(tmp)
        else:
            try:
                result += p.number_to_words(tmp) + ' ' + verbose_signs[v] + ' '
            except IndexError:
                result += verbose_signs[v] + ' '
            else:
                tmp = ''
    is_result_true = eval(s.replace('=', '=='))
    return result, s, True if is_result_true else False



if __name__ == "__main__":
    print(solve(equation))














