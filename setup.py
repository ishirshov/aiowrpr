# This is purely the result of trial and error.
import sys
import codecs

from setuptools import setup
from setuptools import find_packages

import aiowrpr

INSTALL_REQUIRES = [
    'aiodns==2.0.0',
    'aiohttp[speedups]==3.6.2',
    'async-timeout==3.0.1',
    'attrs==19.3.0',
    'brotlipy==0.7.0',
    'cchardet==2.1.5',
    'cffi==1.13.2',
    'chardet==3.0.4',
    'idna==2.8',
    'marshmallow==3.3.0',
    'multidict==4.7.1',
    'pycares==3.1.0',
    'pycparser==2.19',
    'ujson==1.35',
    'webargs==5.5.2',
    'yarl==1.4.2'
]


# Conditional dependencies:
if sys.version_info < (3, 5) or sys.version_info > (3, 8):
    sys.exit(
        f"Sorry, Python {'.'.join(map(str, sys.version_info[:3]))} is not supported"
    )


def long_description():
    with codecs.open('README.md', encoding='utf8') as f_:
        return f_.read()


setup(
    name='aiowrpr',
    version=aiowrpr.__version__,
    description=aiowrpr.__doc__.strip(),
    long_description=long_description(),
    url='https://github.com/ishirshov/aiowrpr',
    download_url='https://github.com/ishirshov/aiowrpr',
    author=aiowrpr.__author__,
    author_email='ildar.shirshov@gmail.com',
    license=aiowrpr.__license__,
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'http = httpie.__main__:main',
            'https = httpie.__main__:main',
        ],
    },
    install_requires=INSTALL_REQUIRES,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development',
        'Topic :: System :: Networking',
        'Topic :: Terminals',
        'Topic :: Text Processing',
        'Topic :: Utilities'
    ],
)