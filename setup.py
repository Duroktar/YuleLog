from setuptools import setup
from codecs import open
from os import path


__version__ = '0.0.3'

SETUP_DIR = path.abspath(path.dirname(__file__))


# Get the long description from the README file
with open(path.join(SETUP_DIR, 'README')) as f:
    long_description = f.read()


# get the dependencies and installs
with open(path.join(SETUP_DIR, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')


install_requires = [x.strip() for x in all_reqs if 'git+' not in x]
dependency_links = [x.strip().replace('git+', '')
                    for x in all_reqs
                    if x.startswith('git+')]


setup(
    name='YuleLog',
    version=__version__,
    url='https://github.com/Duroktar/YuleLog',
    packages=['yule_log'],
    package_data={'yule_log': ['yule_log.ico']},
    license='MIT License',
    author='Scott Doucet',
    author_email='duroktar@gmail.com',
    description='Terminal based X-Mas Yule Log Fireplace',
    long_description=long_description,
    keywords='christmas yule fireplace',
    install_requires=install_requires,
    dependency_links=dependency_links,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Games/Entertainment',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    entry_points={
          'console_scripts': [
              'YuleLog = yule_log.__main__:main'
          ]
      }
)
