# coding: utf-8

from setuptools import setup, find_packages

long_description = """
Con is a French wrapper around the git toolbox

## Examples

* ``git push`` → ``con pulse``
* ``git pull`` → ``con tracte``
* ``git merge`` → ``con bine``
"""

setup(
    name='con_trefacon',
    version="0.0.1",
    license='3-clause BSD',
    description='Con, comme git, mais en français',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="Bastien Gallay",
    author_email="bastien@gallay.org",
    url='http://github.com/elbabass/con',
    py_modules=['con'],
    entry_points={'console_scripts': ['con=con:main']},
    packages=find_packages(exclude=("tests",)),
    classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: BSD License',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Build Tools',
    ]
)
