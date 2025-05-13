#!/usr/bin/python3

def best_score(a_dictionary):
    first = True
    if a_dictionary == {} or a_dictionary is None:
        return None
    else:
        for key, value in a_dictionary.items():
            if first is True:
                best_value = value
                best_key = key
                first = False
            if value > best_value:
                best_value = value
                best_key = key
            else:
                pass
        return best_key
