"""
    Student Evaluator
    Copyright 2014, Jeroen Doggen, jeroendoggen@gmail.com
"""


from __future__ import print_function, division  # We require Python 2.6+

import os
import sys

from logger import Logger


class Grader():
    """ All grading related tasks (analyser.py pushes data, reporter.py pulls data) """
    #TODO: this code is untested! (probably does not run & multi-dim array syntax might be wrong!)
    studentnames_list = []
    grades = []
    grades.append([])
    grades[].append([])

    def __init__(self, settings, logger, setup):
        self.settings = settings
        self.logger = logger
        self.setup = setup

    def write_studentname(self, name):
        """ Write the name of the students to a list """
        self.studentnames_list.append(name)

    def folder_found(self, assignment_number):
        """ Set one assignment to 'found the script folder' """
        grades[number][0].append("1")

    def folder_missing(self, assignment_number):
        """ Set one assignment to 'did not find the script folder' """
        grades[number][0].append("1")

    def assignment_found(self, assignment_number):
        """ Set one assignment to 'found the script file' """
        grades[number][1].append("1")

    def assignment_missing(self, assignment_number):
        """ Set one assignment to 'did not find the script file' """
        grades[number][1].append("1")

    def fail_assignment(self, assignment_number):
        """ Set one assignment to failed """
        grades[number][2].append("0")

    def pass_assignment(self, assignment_number):
        """ Set one assignment to passed """
        grades[number][2].append("1")

