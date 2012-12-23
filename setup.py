from setuptools import setup


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
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
