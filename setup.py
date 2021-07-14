from setuptools import setup
setup(
    name = 'pilot',
    version = '0.1.0',
    packages = ['pilot'],
    entry_points = {
        'console_scripts': [
            'pilot = pilot.__main__:main'
        ]
    })