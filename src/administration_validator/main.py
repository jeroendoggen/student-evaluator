"""
    Administration Validator
    A tool to validate documents in a document archive
    Copyright 2013, Jeroen Doggen, jeroendoggen@gmail.com

    This file is needed to import the module properly

"""

import sys

from administration_validator.validator import AdministrationValidator


def run():
    """Run the main program"""
    validator = AdministrationValidator()
    #assignment_analyser.init()
    validator.run()
    return(validator.exit_value())


if __name__ == "__main__":
    sys.exit(run())
