"""Setup file for Administration Validator

Define the options for the "administration_validator" package
Create source Python packages (python setup.py sdist)
Create binary Python packages (python setup.py bdist)

"""
from distutils.core import setup

from administration_validator import __version__


with open('README.txt') as readme_file:
    LONG_DESCRIPTION = readme_file.read()

setup(name='administration_validator',
      version=__version__,
      description='Administration Validator',
      long_description=LONG_DESCRIPTION,
      author='Jeroen Doggen',
      author_email='jeroendoggen@gmail.com',
      url='none',
      packages=['administration_validator'],
      package_data={'administration_validator': ['*.py', '*.conf']},
      license='LGPL-v2',
      platforms=['Linux'],
      )
