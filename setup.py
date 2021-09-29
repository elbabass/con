# coding: utf-8

import re
from os.path import dirname, join, abspath

from setuptools import setup

VERSION = re.search(
    r"__version__\s=\s'(\d\.\d\.\d)'",
    open(abspath(join(dirname(__file__), 'con.py'))).read()
).group(1)

setup(
    name='con',
    version=VERSION,
    license='3-clause BSD',
    description='Con, comme git, mais en français',
    author="Bastien Gallay",
    author_email="bastien@gallay.org",
    url='http://github.com/elbabass/con',
    py_modules=['con'],
    entry_points={'console_scripts': ['con=con:main']},
    classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: BSD License',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Build Tools',
    ]
)
