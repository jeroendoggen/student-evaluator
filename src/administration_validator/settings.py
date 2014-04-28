"""
    Administration Validator
    Copyright 2013, Jeroen Doggen, jeroendoggen@gmail.com
"""

# TODO: report all students that hand in the assignment after the deadline
# TODO: ...

import os
import ConfigParser


class Settings:
    """ Contains all the tools to analyse Blackboard assignments """
    logfile = "administration_validator.log"
    summary_file = 'summary.log'
    script_path = os.getcwd()
    input_path = script_path
    output_path = script_path 
    Config = ConfigParser.ConfigParser()
    Log = ConfigParser.ConfigParser()
    working_dir = os.getcwd()
    folders_list = []
    subfolders_list = []

    def __init__(self):
        self.read_config_file("settings.conf")

    def config_section_map(self, section):
        """ Helper function to read config settings """
        dict1 = {}
        options = self.Config.options(section)
        for option in options:
            try:
                dict1[option] = self.Config.get(section, option)
                if dict1[option] == -1:
                    DebugPrint("skip: %s" % option)
            except:
                print("exception on %s!" % option)
                dict1[option] = None
                sys.exit(1)
        return dict1

    def read_config_file(self, filename):
        """ Read the config  """
        try:
            self.Config.read(filename)
            self.folder_prefix = self.config_section_map("Config")['prefix']
            for number, folder in enumerate(self.Config.items( "Folders" )):
                self.folders_list.append(folder[1])
            for number, subfolder in enumerate(self.Config.items( "SubFolders" )):
                self.subfolders_list.append(subfolder[1])
        except AttributeError:
            #TODO: this does not work!! (AttributeError or KeyError needed? both?)
            print("Error while processing settings.conf")
            sys.exit(1)