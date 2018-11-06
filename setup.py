from setuptools import setup

setup(name='Kolbmann Python Package',
     version='0.1',
     description='Read a matrix asnd run BLAST searches',
     url='TBD',
     author='Christina Kolbmann',
     author_email='christina.kolbmann@selu.edu',
     license='MIT',
     packages=['kolbmannpythonpackage'],
     install_requires=[
         'dendropy',
         'biopython',
         'pandas'
     ],
     long_description=open('README.txt').read(),
zip_safe=True)