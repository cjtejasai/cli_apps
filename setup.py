from setuptools import setup

setup(
    name='jarvis',
    version='0.1',
    author="cjtejasai",
    author_email="cjtejasai@gmail.com",
    description="A command line interface for displaying system ",
    py_modules=['jarvis'],
    install_requires=[
        'click',
        'psutil',
    ],
    entry_points='''
        [console_scripts]
        jarvis=jarvis:jarvis
    ''',
)
