# To give credit where credit is due:
# This problem was taken from the ACMICPC-Northwest Regional Programming Contest.
# Thank you problem writers.
#
# You are helping an archaeologist decipher some runes. He knows that this ancient
# society used a Base 10 system, and that they never start a number with a leading zero.
# He's figured out most of the digits as well as a few operators, but he needs your help to figure out the rest.
#
# The professor will give you a simple math expression, of the form
#
# [number][op][number]=[number]
# He has converted all of the runes he knows into digits. The only operators he knows
# are addition (+),subtraction(-), and multiplication (*), so those are the only ones
# that will appear. Each number will be in the range from -1000000 to 1000000, and will
# consist of only the digits 0-9, possibly a leading -, and maybe a few ?s.
# If there are ?s in an expression, they represent a digit rune that the professor
# doesn't know (never an operator, and never a leading -). All of the ?s in an expression
# will represent the same digit (0-9), and it won't be one of the other given digits in
# the expression. No number will begin with a 0 unless the number itself is 0,
# therefore 00 would not be a valid number.
#
# Given an expression, figure out the value of the rune represented by the question mark.
# If more than one digit works, give the lowest one. If no digit works, well, that's bad
# news for the professor - it means that he's got some of his runes wrong. output -1 in that case.
#
# Complete the method to solve the expression to find the value of the unknown rune.
# The method takes a string as a paramater repressenting the expression and will return an int
# value representing the unknown rune or -1 if no such rune exists.
import re

def solve_runes(runes: str) -> int:
    print(runes)
    operator_pttrn = r"[\+\-\*]"
    statement, result = runes.split("=")
    left_op, right_op = re.split(operator_pttrn, statement[1:], maxsplit=1)
    left_op = statement[0] + left_op
    operator_ = re.search(operator_pttrn, statement[1:]).group()
    known = set(re.findall(r"\d", runes))
    commands = {"+": lambda x, y: x + y,
                "-": lambda x, y: x - y,
                "*": lambda x, y: x * y
                }
    if any((left_op.replace("?", "0").startswith("00"),
            right_op.replace("-", "").replace("?", "0").startswith("00"),
            result.replace("-", "").replace("?", "0").startswith("0"))):
        search_series = set("123456789")
    else:
        search_series = set("0123456789")
    if result.replace("?", "0") == "0":
        search_series |= set("0")
    search_series = sorted(search_series - known)
    for digit in search_series:
        left = int(left_op.replace("?", digit))
        right = int(right_op.replace("?", digit))
        res = int(result.replace("?", digit))
        if commands[operator_](left, right) == res:
            return int(digit)
    return -1


def solve_runes_smart(runes):
    for d in sorted(set("0123456789") - set(runes)):
        to_test = runes.replace("?", d)
        if re.search(r'([^\d]|\b)0\d+', to_test):
            continue
        l, r = to_test.split("=")
        if eval(l) == eval(r):
            return int(d)
    return -1

print(solve_runes("-?56373--9216=-?47157"), "should 8")

