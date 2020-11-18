#!/usr/bin/env python

#from distutils.core import setup
#
#setup(name = 'Distutils',
#      version = '1.0.0',
#      description = 'I-Frag',
#      author = 'Carter Lantz',
#      author_email = 'internalfragments.loolab@gmail.com',
#      url = 'Website',
#      packages = ['Pillow', 'certifi', 'cycler', 'kiwisolver', 'matplotlib', 'numpy', 'pandas', 'pip', 'pyparsing', 'python-dateutil', 'pytz', 'scipy', 'seaborn', 'six', 'tqdm'],
#      )

import os
packages = ['Pillow', 'certifi', 'cycler', 'kiwisolver', 'matplotlib', 'numpy', 'pandas', 'pip', 'pyparsing', 'python-dateutil', 'pytz', 'scipy', 'seaborn', 'six', 'tqdm']
for package in packages:
      print(package)
      os.system("python -m pip install "+str(package))
