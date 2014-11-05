"""
    Student Evaluator: add users
    Copyright 2014, Jeroen Doggen, jeroendoggen@gmail.com
"""

from __future__ import print_function, division  # We require Python 2.6+

import sys
import os

number = 5
username_prefix = "s"

def run(number):
    """Create user accounts on the system """
    os.system("addgroup students")
    for x in range(0, number):
        username = username_prefix + str(x)
        print(username)
        # password: 'student'
        os.system("useradd -p  SNSr7/A1BYa12 -g students " + username )
        os.system("mkdir /home/" + username)
        os.system("chown "+ username + ":students " + "/home/" + username )
        os.system("usermod " + username + " -s /bin/rbash")
        os.system("usermod " + username + " -g students")

if __name__ == "__main__":
    sys.exit(run(number))