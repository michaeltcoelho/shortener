#encoding:utf-8
from distutils.core import setup
from setuptools import find_packages


REQUIREMENTS = [i.strip() for i in open("requirements.txt").readlines()
                            if not i.startswith("http")]

long_description = open("README.md").read()

setup(name="shortener",
      version="0.0.1",
      license="MIT",
      description = "An url shortener",
      url="https://github.com/michaeltcoelho/shortener",
      author="Michael Coelho",
      author_email="michael.tcoelho+shortener@gmail.com",
      packages=find_packages(),
      long_description=long_description,
      download_url="https://github.com/michaeltcoelho/shortener/tarball/master",
      install_requires=REQUIREMENTS,
      include_package_data=True,
      zip_safe=False)