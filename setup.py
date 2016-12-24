from setuptools import setup

setup(
    name='YuleLog',
    version='0.0.1',
    url='https://github.com/Duroktar/YuleLog',
    packages=['yule_log'],
    package_data = {'yule_log': ['yule_log.ico']},
    license='MIT License',
    author='Scott Doucet',
    author_email='duroktar@gmail.com',
    description='Terminal based X-Mas Yule Log Fireplace',
    install_requires=["asciimatics"],
    keywords='christmas yule fireplace,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Games/Entertainment',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
    entry_points={
          'console_scripts': [
              'YuleLog = yule_log.__main__:main'
          ]
    },
)
