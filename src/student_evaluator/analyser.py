"""
    Student Evaluator
    Copyright 2014, Jeroen Doggen, jeroendoggen@gmail.com
"""


from __future__ import print_function, division  # We require Python 2.6+

import os
import sys

from logger import Logger


class Analyser():
    """ Analyse all the documents """
    txt_files_list = []

    def __init__(self, settings, logger, reporter, setup, grader):
        self.settings = settings
        self.logger = logger
        self.reporter = reporter
        self.setup = setup
        self.grader = grader

    def run(self):
        """ Run all tests, staring narrowing down the scope step by step """
        #self.check_folders()
        self.get_studentname()
        self.check_file("dummy filename")

    def check_assignment(self, name):
        self.check_folder(name)
        self.check_file(name)
        self.analyse(name)

    def check_folder(self, folder):
        path = os.path.join(self.setting.input_path, self.settings.folder_prefix, folder)
        if (os.path.isdir(path)):
            

    def check_folder(self, filename):
        """ Check if a file exists """
        pass

    def check_file(self, filename):
        """ Check if a file exists """
        pass

    def get_studentname(self):
        """Create user accounts on the system """
        for x in self.setup.studentnames_list:
            filename = "/home/" + x + "/naam"
            try:
                with open(filename) as f:
                    first_line = f.readline()
                    self.grader.write_studentname(first_line)
                    #print (first_line)
            except:
                #print ("No name provided by: " + x)
                self.grader.write_studentname(first_line)

    def check_access_rights(self, filename, rights):
        """ Check if a file/folder has the correct access rights """
