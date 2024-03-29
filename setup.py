# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


try:
    from pypandoc import convert
except ImportError:
    def convert(filename, fmt):
        with open(filename) as fd:
            return fd.read()


DESCRIPTION = 'Simple Django CMS Metatags Plugin'

CLASSIFIERS = [
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Development Status :: 3 - Alpha',
]


setup(
    name='django-cmsmetatags',
    version='0.4.2a',
    author='Alaric Mägerle',
    author_email='info@rouxcode.ch',
    description=DESCRIPTION,
    long_description=convert('README.md', 'rst'),
    url='https://github.com/rouxcode/django-cmsmetatags',
    license='MIT',
    keywords=['django'],
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    install_requires=[
        'django>=3.2'
    ],
    packages=find_packages(exclude=['example', 'docs']),
    include_package_data=True,
    zip_safe=False,
)
