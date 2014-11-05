"""
    Student Evaluator: scan the name files
    Copyright 2014, Jeroen Doggen, jeroendoggen@gmail.com
"""

from __future__ import print_function, division  # We require Python 2.6+

import sys
import os
import datetime

number = 100
username_prefix = "s"
time = datetime.datetime.now()

def run(number):
    """Scan for user accounts on the system """
    os.system("mv /var/www/misc/usernames /var/www/misc/usernames_old" + str(time.minute))
    os.system("cd /home")
    for x in range(0, number):
        username = username_prefix + str(x)
        print(username)
        os.system("cd /home/" + username )
        os.system("pwd")
        file = "/home/" + username + "/naam"
        os.system("echo " + username + ">>/var/www/misc/usernames")
        os.system("cat " + file + ">>/var/www/misc/usernames" )

if __name__ == "__main__":
    sys.exit(run(number))

