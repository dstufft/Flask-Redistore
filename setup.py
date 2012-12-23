import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest

        sys.exit(pytest.main(self.test_args))


setup(
    name="Flask-Redistore",
    version="1.0",
    url="",
    license="BSD",
    author="Donald Stufft",
    author_email="donald.stufft@gmail.com",
    description="Adds Redis support to your Flask applications",
    long_description=open("README.rst").read(),
    py_modules=["flask_redistore"],
    zip_safe=False,
    include_package_data=True,
    platforms="any",
    install_requires=[
        "Flask",
        "redis",
    ],
    extras_require={"tests": ["pytest", "pretend"]},
    tests_require=["pytest", "pretend"],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    cmdclass={"test": PyTest},
)
