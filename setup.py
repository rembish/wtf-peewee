#!/usr/bin/env python
from setuptools import setup


setup(
    name='wtf-peewee',
    version='0.2.4',
    url='https://github.com/rembish/wtf-peewee',
    license='MIT',
    author='Charles Leifer',
    author_email='coleifer@gmail.com',
    maintainer='Aleksey Rembish',
    maintainer_email='alex@rembish.org',
    description='WTForms integration for peewee models',
    packages=['wtfpeewee'],
    zip_safe=True,
    platforms='any',
    install_requires=[
        'peewee>=2.0.0', 'wtforms',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    test_suite='runtests.runtests'
)
