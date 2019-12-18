from setuptools import setup, find_packages
from codecs import open
from os import path
import re

here = path.abspath(path.dirname(__file__))

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('tiktok_scraper/__init__.py').read(),
    re.M
    ).group(1)

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
        name = 'tiktok-scraper',
        packages = find_packages(), # this must be the same as the name above
        version = version,
        description = 'Scrapes TikTok videos',
        long_description = long_description,
        author = 'joeyism',
        author_email = 'joeyism@gmail.com',
        entry_points = {
            "console_scripts": ['tiktok-scraper = tiktok_scraper.cli:main']
        },
        url = 'https://github.com/joeyism/tiktok-scraper', # use the URL to the github repo
        download_url = 'https://github.com/joeyism/tiktok-scraper/archive/{}.tar.gz'.format(version),
        keywords = ['tik', 'tok', 'tiktok', 'scraper', 'download', 'video'], 
        install_requires = [package[:-2] for package in open("requirements.txt", "r").readlines()],
        classifiers = [],
        )
