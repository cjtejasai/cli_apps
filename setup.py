from setuptools import setup

setup(
    name='jarvis',
    version='0.1',
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
