"""
Your calculation isn't quite right.
It looks like some of the digits are actually spelled out with letters:
one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values?
"""

digits = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}

def get_first_digit(s: str) -> str:
    for i in range(len(s)):
        if s[i].isnumeric():
            return s[i]
        for word in digits:
            if s[i : i + len(word)] == word:
                return digits[word]

def get_last_digit(s: str) -> str:
    for i in range(len(s) - 1, -1, -1):
        if s[i].isnumeric():
            return s[i]
        for word in digits:
            if s[i - len(word) : i] == word:
                return digits[word]

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
    