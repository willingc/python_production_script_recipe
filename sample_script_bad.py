"""
Don't use scripts like this in production!
"""

import random
import sys
import time


result = int(sys.argv[1]) + random.randint(0, 9)


if result < 10:
    print(result)
    time.sleep(2)  # Simulate a delay while the script works.
