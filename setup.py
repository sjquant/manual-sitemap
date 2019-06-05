import io

from setuptools import setup
from manual_sitemap.__version__ import version

with io.open("README.rst", mode='r', encoding='utf-8') as rm:
    long_description = rm.read()

setup(
    name='manual-sitemap',
    version=version,
    author='SJQuant',
    license="MIT",
    author_email='seonujang92@gmail.com',
    description=(
        'manually create sitemap config and generate sitemap using it'
    ),
    url='https://github.com/sjquant/manual-sitemap',
    long_description=long_description,
    packages=['manual_sitemap'],
    keywords=['sitemap', 'xml'],
    entry_points={
        "console_scripts": [
            "manual-sitemap = manual_sitemap.main:create_sitemap"
        ]
    },
    install_requires=['click>=7.0'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
