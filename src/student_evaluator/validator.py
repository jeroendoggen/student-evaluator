"""
    Student Evaluator
    Copyright 2014, Jeroen Doggen, jeroendoggen@gmail.com
"""


from __future__ import print_function, division  # We require Python 2.6+

import os

from student_evaluator.settings import Settings
from student_evaluator.logger import Logger
from student_evaluator.analyser import Analyser
from student_evaluator.reporter import Reporter


class StudentEvaluator:
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