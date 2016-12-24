from setuptools import setup

setup(
    name='YuleLog',
    version='0.0.1',
    url='https://github.com/Duroktar/YuleLog',
    packages=['yule_log'],
    package_data = {'yule_log': ['yule_log.ico']},
    license='MIT',
    author='Scott Doucet',
    author_email='duroktar@gmail.com',
    description='Terminal based X-Mas Yule Log Fireplace',
    install_requires=["asciimatics"],
    entry_points={
          'console_scripts': [
              'YuleLog = yule_log.__main__:main'
          ]
      }
)
