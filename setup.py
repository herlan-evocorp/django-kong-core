import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

with open('requirements/requirements.txt') as f:
    install_requirements = f.readlines()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-kong-core',
    version='0.8.5.6',
    include_package_data=True,
    license='BSD License',  # example license
    description='Django Kong Core',
    long_description=README,
    # url='https://www.example.com/',
    install_requires=install_requirements,
    author='Herlan Assis',
    author_email='herlan@evocorp.com.br',
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.2.5',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
