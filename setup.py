import os
import sys
from setuptools import find_packages, setup

VERSION = "1.0.2"
LONG_DESCRIPTION = """
.. image:: http://pinaxproject.com/pinax-design/patches/pinax-forums.svg
    :target: https://pypi.python.org/pypi/pinax-forums/

============
Pinax Forums
============

.. image:: https://img.shields.io/pypi/v/pinax-forums.svg
    :target: https://pypi.python.org/pypi/pinax-forums/

\ 

.. image:: https://img.shields.io/circleci/project/github/pinax/pinax-forums.svg
    :target: https://circleci.com/gh/pinax/pinax-forums
.. image:: https://img.shields.io/codecov/c/github/pinax/pinax-forums.svg
    :target: https://codecov.io/gh/pinax/pinax-forums
.. image:: https://img.shields.io/github/contributors/pinax/pinax-forums.svg
    :target: https://github.com/pinax/pinax-forums/graphs/contributors
.. image:: https://img.shields.io/github/issues-pr/pinax/pinax-forums.svg
    :target: https://github.com/pinax/pinax-forums/pulls
.. image:: https://img.shields.io/github/issues-pr-closed/pinax/pinax-forums.svg
    :target: https://github.com/pinax/pinax-forums/pulls?q=is%3Apr+is%3Aclosed

\ 

.. image:: http://slack.pinaxproject.com/badge.svg
    :target: http://slack.pinaxproject.com/
.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target: https://opensource.org/licenses/MIT

\ 

``pinax-forums`` is an extensible forums app for Django and Pinax. It is
focused on core forum functionality and hence is expected to be combined with
other Pinax apps for broader features.

See ``pinax-project-forums`` for a full Django project incorporating numerous
apps with the goal of providing an out of the box forums solution.

Supported Django and Python Versions
------------------------------------

+-----------------+-----+-----+-----+
| Django / Python | 3.4 | 3.5 | 3.6 |
+=================+=====+=====+=====+
|  1.11           |  *  |  *  |  *  |
+-----------------+-----+-----+-----+
|  2.0            |  *  |  *  |  *  |
+-----------------+-----+-----+-----+
"""

# Publish Helper.
if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist bdist_wheel upload')
    sys.exit()

setup(
    author="flytrap",
    author_email="hiddenstat@gmail.com",
    description="an extensible forum app for Django and Pinax",
    name="flytrap-forums",
    long_description=LONG_DESCRIPTION,
    version=VERSION,
    url="http://github.com/flytrap/pinax-forums/",
    license="MIT",
    packages=find_packages(),
    package_data={
        "forums": []
    },
    install_requires=[
        "django>=1.11"
    ],
    test_suite="runtests.runtests",
    tests_require=[
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)
