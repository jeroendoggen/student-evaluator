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
        self.userslist = []
        self.create_list("s", self.settings.number_of_students)

        if self.settings.create_users == '1':
            self.create_users()
            self.info("Users created: " + str(self.settings.number_of_students))
        if self.settings.remove_users == '1':
            self.remove_users()
            self.info("Users removed: " + str(self.settings.number_of_students))

    def create_list(self, username_prefix, number):
        """Create a list of usernames to be reused later"""
        for x in range(0, number):
            username = username_prefix + str(x)
            self.userslist.append(username)

    def create_users(self):
        """Create user accounts on the system """
        #TODO: only if it does not exist
        os.system("addgroup students")
        for x in self.userslist:
            print("Adding user: " + x)
            # password = 'student'
            os.system("useradd -p  SNSr7/A1BYa12 -g students " + x)
            os.system("mkdir /home/" + x)
            os.system("chown " + x + ":students " + "/home/" + x)

    def remove_users(self):
        """Remove the user accounts (at the end) """
        for x in self.userslist:
            print("Removing user: ")
            os.system("deluser --remove-home " + x)

    def info(self, message):
        self.logger.info(message)
