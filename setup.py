import os
from setuptools import setup, find_packages

import feedgrabber

setup(name='django-feedgrabber',
      version=feedgrabber.__version__,
      
      description='A RSS/Atom feeds grabber, for your Django websites.',
      long_description=open(os.path.join('README.rst')).read(),
      keywords='django, rss, atom',

      author=feedgrabber.__author__,
      author_email=feedgrabber.__email__,
      url=feedgrabber.__url__,
      license=feedgrabber.__license__,

      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'FeedParser',
          ],

      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Web Environment',
          'Programming Language :: Python',
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'License :: OSI Approved :: BSD License',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Framework :: Django',],
      )



