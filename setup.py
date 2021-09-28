from setuptools import setup

setup(
    name='con',
    version='0.0.1',
    packages=['con'],
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
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Build Tools',
        ]
)
