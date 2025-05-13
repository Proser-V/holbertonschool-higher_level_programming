#!/usr/bin/python3

def roman_to_int(roman_string):
    roman_numerals = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    i = 0
    result = 0
    if roman_string is None or type(roman_string) != str:
        return 0
    else:
        while i < len(roman_string):
            key = roman_string[i]
            if i + 1 >= len(roman_string):
                if key in roman_numerals:
                    result += roman_numerals[key]
            else:
                if key in roman_numerals:
                    next_key = roman_string[i + 1]
                    if next_key in roman_numerals:
                        if roman_numerals[next_key] > roman_numerals[key]:
                            result -= roman_numerals[key]
                        else:
                            result += roman_numerals[key]
            i += 1
    return result