#!/usr/bin/python3
import re
import inflect


def solve(s):
    p = inflect.engine()
    nums = '01234567890'
    signs = '+-*/= '
    allowed_chars = nums + signs
    verbose_signs = {'+': 'plus', '-': 'minus', '*': 'multiple by', '/': 'divide by', '=': 'equals'}
    
    if any(i not in allowed_chars for i in s):
        return "invalid input"
    if '=' not in s or not any(i in '+-*/' for i in s):
        return "invalid input"

    s = s.strip()

    s = ''.join(s.split())

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
    #return result, s, True if is_result_true else False
    return result


class TestClass:

    def test_simple(self):
        eq = '3 + 7 = 10'
        assert solve(eq) == 'three plus seven equals ten'

    def test_minus_or_plus_first(self):
        eq1 = '-73 + 70= -3'
        eq2 = '+73 + 70= -3'
        assert solve(eq1) == 'minus seventy-three plus seventy equals minus three'
        assert solve(eq2) == 'plus seventy-three plus seventy equals minus three'

    def test_multiple_values_before_and_after_equal_sign(self):
        eq = '12 - 6 = 18 / 3'
        assert solve(eq) == 'twelve minus six equals eighteen divide by three'

    def test_multiple_spaces(self):
        eq = '12     + 7=         19'
        assert solve(eq) == 'twelve plus seven equals nineteen'

    def test_invalid_input(self):
        eq1 = '12 + 2k = 45.'
        eq2 = '12 + 45 34'
        eq3 = '12 = 12'
        assert all(solve(e) == 'invalid input' for e in [eq1, eq2, eq3])


if __name__ == "__main__":
    equation = input("Enter the equation: ")
    print(solve(equation))
