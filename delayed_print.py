import time
import sys

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.02)
        if c == "," or c == ";" or c == ":":
            time.sleep(0.2)
        if c == "." or c == "?" or c == "!":
            time.sleep(0.4)
        if c == " ":
            time.sleep(0.05)