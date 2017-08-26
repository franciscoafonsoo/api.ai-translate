# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='api_ai_translate',
    version='0.1.0',
    description='Translate API.AI agents.',
    long_description=readme,
    author='Francisco Pires',
    author_email='afonso.fcul@gmail.com',
    url='https://github.com/franciscoafonsoo/api_ai_translate',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=["nose", "sphinx", "graphviz", "numpy", "pyqt5"],
    dependency_links=[
        "https://bitbucket.org/fchampalimaud/logging-bootstrap/get/master.zip",
        "https://github.com/UmSenhorQualquer/pysettings/archive/master.zip",
        "https://github.com/UmSenhorQualquer/pyforms/archive/master.zip"
    ],
)