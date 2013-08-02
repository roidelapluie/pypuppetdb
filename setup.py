import sys
import os
import codecs

from setuptools import setup
from setuptools.command.test import test as TestCommand

from pypuppetdb import __version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()


class PyTest(TestCommand):

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['-pep8 -m unit', ]
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)

with codecs.open('README.rst', encoding='utf-8') as f:
    README = f.read()

with codecs.open('CHANGELOG.rst', encoding='utf-8') as f:
    CHANGELOG = f.read()

packages = [
    'pypuppetdb',
    'pypuppetdb.api',
    ]

test_requires = [
    'pytest',
    'pytest-pep8',
    'httpretty',
    'pytest-httpretty',
]

setup(
    name='pypuppetdb',
    version=__version__,
    author='Daniele Sluijters',
    author_email='daniele.sluijters+pypi@gmail.com',
    packages=packages,
    url='https://github.com/nedap/pypuppetdb',
    license=open('LICENSE').read(),
    description='Library for working with the PuppetDB REST API.',
    long_description=README + u'\n' + CHANGELOG,
    package_data={'': ['LICENSE', 'CHANGELOG.rst', ], },
    include_package_data=True,
    keywords='puppet puppetdb',
    tests_require=test_requires,
    cmdclass={'test': PyTest},
    install_requires=[
        "requests >= 1.2.3",
        "pytz == 2013b",
        ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Libraries'
        ],
    )