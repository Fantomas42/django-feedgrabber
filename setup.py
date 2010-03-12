from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='django-feedgrabber',
      version=version,
      
      description='A RSS/Atom feeds grabber, for your Django websites.',
      long_description=open(os.path.join('README.rst')).read(),
      keywords='django, rss, atom',

      author='Fantomas42',
      author_email='fantomas42@gmail.com',
      url='http://github.com/Fantomas42/django-feedgrabber',
      license='BSD License',

      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
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



