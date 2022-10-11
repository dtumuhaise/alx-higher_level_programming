#!/usr/bin/python3

def safe_print_division(a, b):
    div = 0
    try:
        div = a / b
    except (ZeroDivisionError, TypeError):
        return None
    finally:
        if b == 0:
            print("Inside Result: None")
        else:
            print("Inside result: {}".format(div))
    return div