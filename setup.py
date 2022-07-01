from setuptools import setup

setup(
   name='main',
   version='1.0',
   description='visualizacion de datafremes 2d',
   author='Jhonier Menesees',
   author_email='jhoniermeneses2001@gamil.com',
   packages=['main'],
   install_requires=[
         'matplotlib',
         'sklearn',
         'pandas',
         'pyqt5'],
)
