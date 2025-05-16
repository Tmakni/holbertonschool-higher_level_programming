#!/usr/bin/python3
def roman_to_int(roman_string):
    romans = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    if roman_string is None or not isinstance(roman_string, str):
        return 0

    total = 0
    i = 0

    while i < len(roman_string):
        current = romans[roman_string[i]]

        if i + 1 < len(roman_string):
            next_val = romans[roman_string[i + 1]]

            if current < next_val:
                total += next_val - current
                i += 2
                continue

        total += current
        i += 1

    return total
