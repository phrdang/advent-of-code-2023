"""
The newly-improved calibration document consists of lines of text;
each line originally contained a specific calibration value that the
Elves now need to recover. On each line, the calibration value can be
found by combining the first digit and the last digit (in that order)
to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
In this example, the calibration values of these four lines are 12, 38, 15, and 77.
Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?
"""

def get_first_digit(s: str) -> str:
    """
    >>> get_first_digit('1abc2')
    '1'
    >>> get_first_digit('treb7uchet')
    '7'
    """
    for char in s:
        if char.isnumeric():
            return char

def get_last_digit(s: str) -> str:
    """
    >>> get_last_digit('1abc2')
    '2'
    >>> get_last_digit('treb7uchet')
    '7'
    """
    for i in range(len(s) - 1, -1, -1):
        if s[i].isnumeric():
            return s[i]

def get_calibration_value(line: str) -> int:
    first_digit = get_first_digit(line)
    last_digit = get_last_digit(line)
    return int(f'{first_digit}{last_digit}')

if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        total = 0
        for line in f:
            total += get_calibration_value(line)
        print(total)
    