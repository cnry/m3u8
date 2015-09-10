from os.path import dirname, abspath, join, exists
from setuptools import setup

long_description = None
if exists("README.rst"):
    long_description = open("README.rst").read()

install_reqs = [req for req in open(abspath(join(dirname(__file__), 'requirements.txt')))]

setup(
    name="cnry-m3u8",
    author='Canary Engineering Team',
    author_email='gabriel@nacaolivre.org',
    version="0.2.7",
    zip_safe=False,
    include_package_data=True,
    install_requires=install_reqs,
    packages=["m3u8"],
    url="https://github.com/cnry/m3u8",
    description="Canary's fork of the python m3u8 parser by globo.com (github.com/globocom/m3u8)",
    long_description=long_description
    )
