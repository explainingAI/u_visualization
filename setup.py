from setuptools import setup

setup(
   name='main',
   version='1.0',
   description='visualizacion de datafremes 2d',
   author='Jhonier Menesees',
   author_email='jhoniermeneses2001@gamil.com',
   packages=['main'],  # same as name
   install_requires=['matplotlib', 'sklearn', 'pandas', 'pyqt5'],  # external packages as dependencies  pip install pyqt5
)
