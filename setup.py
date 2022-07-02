from setuptools import setup, find_packages
setup(
    name = 'MacroX',
    version = '0.0.1',
    license = 'MIT',
    description = 'A python macro tool',
    author = 'Wrench56',
    author_email = 'dmarkreg@gmail.com',
    url = 'https://github.com/Wrench56/MacroX',
    install_requires = ['rich'],
    long_description = 'Please find more information on my Github page!',
    entry_points={
         "console_scripts": [
            "macrox=src.macrox:main"
        ]
    },
    packages=find_packages()
)