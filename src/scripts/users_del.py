"""
    Add system users
    Copyright 2014, Jeroen Doggen, jeroendoggen@gmail.com
"""

from __future__ import print_function, division  # We require Python 2.6+

import sys
import os

number = 100
username_prefix = "s"

def run(number):
    """Create user accounts on the system """
    #os.system("addgroup students")
    for x in range(0, number):
        username = username_prefix + str(x)
        print("Removing user: " + username)
        os.system("userdel " + username )
        os.system("rm -rf /home/" + username)

if __name__ == "__main__":
    sys.exit(run(number))
