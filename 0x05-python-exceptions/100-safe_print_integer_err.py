#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".formart(value))
    except Exception as i:
        sys.stderr.write("Exception: {}\n".format(i))
        return False
    else:
        return True