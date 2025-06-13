#!/usr/bin/env python
from setuptools import setup, find_packages


setup(name='tap-airtable',
      version='0.0.3',
      description='Singer.io tap for extracting data from the Airtable API',
      author='AIME Mentorinng',
      url='https://singer.io',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      py_modules=['tap_airtable'],
      install_requires=[
          'backoff>=1.3.2',
          'certifi>=2023.7.22',
          'chardet>=3.0.4',
          'idna>=2.7',
          'jsonschema>=2.6.0',
          'pendulum>=1.2.0',
          'python-dateutil>=2.8.2',
          'pytz>=2018.4',
          'pytzdata>=2018.7',
          'requests>=2.31.0',
          'simplejson>=3.11.1',
          'singer-python>=5.12.0',
          'python-slugify>=4.0.1',
          'six>=1.16.0',
          'tzlocal>=1.5.1',
          'urllib3>=1.26.5',
          'typing-extensions>=4.0.0',
          'importlib-metadata>=4.0.0'
      ],
      entry_points='''
          [console_scripts]
          tap-airtable=tap_airtable:main
      ''',
      packages=find_packages(),
      include_package_data=True,
      )
