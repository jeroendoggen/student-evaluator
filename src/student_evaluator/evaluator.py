"""
    Student Evaluator
    Copyright 2014, Jeroen Doggen, jeroendoggen@gmail.com
"""


from __future__ import print_function, division  # We require Python 2.6+

import os

from settings import Settings
from logger import Logger
from analyser import Analyser
from reporter import Reporter
from setup import Setup
from grader import Grader


class StudentEvaluator:
    """ Contains all the tools to analyse assignments """
    errors = 0

    def __init__(self):
        self.settings = Settings()
        self.logger = Logger(self.settings.logfile)
        self.reporter = Reporter(self.settings)
        self.setup = Setup(self.settings, self.logger)
        self.grader = Grader(self.settings, self.logger, self.setup)
        self.analyser = Analyser(self.settings, self.reporter, self.logger, self.setup, self.grader)


    def run(self):
        #""" Run the program (call this from main) """
        self.analyser.run()
        #self.reporter.run()

    def exit_value(self):
        #"""TODO: Generate the exit value for the application."""
        if (self.errors == 0):
            return 0
        else:
            return 42
