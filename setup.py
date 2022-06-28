"""
Setup the python package script with setuptools.

"""
from setuptools import setup, find_packages

setup(
    name='acc_viz',
    version='0.1',
    packages=find_packages(),
    setup_requires=['wheel'],
    install_requires=[
        'audiolazy',
        'gTTS',
        'matplotlib',
        'numpy',
        'pandas',
        'playsound',
        'pygame',
        'seaborn',
        'MIDIUtil'
    ],
    entry_points='''
        [console_scripts]
        accessible_data_visualizations=main:main
    ''',
)
