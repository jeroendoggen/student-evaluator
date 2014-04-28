"""
    Administration Validator
    Copyright 2013, Jeroen Doggen, jeroendoggen@gmail.com
"""

# TODO: report all students that hand in the assignment after the deadline
# TODO: ...


from __future__ import print_function, division  # We require Python 2.6+

import os

from administration_validator.settings import Settings
from administration_validator.logger import Logger
from administration_validator.analyser import Analyser
from administration_validator.reporter import Reporter


class AdministrationValidator:
    """ Contains all the tools to analyse Blackboard assignments """
    errors = 0

    def __init__(self):
        self.settings = Settings()
        self.mylogger = Logger(self.settings.logfile)
        self.reporter = Reporter(self.settings)
        self.analyser = Analyser(self.settings, self.reporter, self.mylogger)

    def run(self):
        #""" Run the program (call this from main) """
        self.analyser.run()
        self.reporter.run()

    def exit_value(self):
        #"""TODO: Generate the exit value for the application."""
        if (self.errors == 0):
            return 0
        else:
            return 42