import os
from setuptools import setup

setup(name='pnr',
      version='1.0.0',
      description='Check your train PNR status',
      keywords='Train Indian PNR check command line',
      url='http://github.com/akashnimare/pnrstatus/',
      author='Akash Nimare',
      author_email='svnitakash@gmail.com',
      license='MIT',
      packages=['pnr'],
      entry_points = {
        'console_scripts': ['pnr=pnr.auto:pnr'],
        },
      install_requires=[
            'requests','BeautifulSoup'
      ],
      zip_safe=False)

