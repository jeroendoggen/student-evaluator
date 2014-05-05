"""
    Student Evaluator
    Copyright 2014, Jeroen Doggen, jeroendoggen@gmail.com
"""

from __future__ import print_function, division  # We require Python 2.6+

import sys
import os


class Setup():
    """ Setup class: pre-configure the system """

    def __init__(self, settings, logger):
        self.settings = settings
        self.logger = logger
        if self.settings.create_users == '1':
            self.create_users("s", self.settings.number_of_students)
            self.info("Users created: " + str(self.settings.number_of_students))
        if self.settings.remove_users == '1':
            self.remove_users("s", self.settings.number_of_students)
            self.info("Users removed: " + str(self.settings.number_of_students))

    def create_users(self, username_prefix, number):
        """Create user accounts on the system """
        #TODO: only if it does not exist
        os.system("addgroup students")
        for x in range(0, number):
            username = username_prefix + str(x)
            print("Adding user: " + username)
            # password = 'student'
            os.system("useradd -p  SNSr7/A1BYa12 -g students " + username )
            os.system("mkdir /home/" + username)
            os.system("chown "+ username + ":students " + "/home/" + username )

    def remove_users(self, username_prefix, number):
        """Remove the user accounts (at the end) """
        for x in range(0, number):
            print("Removing user: ")
            username = username_prefix + str(x)
            os.system("deluser --remove-home " + username )

    def info(self, message):
        self.logger.info(message)
