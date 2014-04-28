"""
    Student Evaluator
    Copyright 2014, Jeroen Doggen, jeroendoggen@gmail.com
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
