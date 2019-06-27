from setuptools import find_packages
from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='comap_hr_scan',
    description='Scanned documents sorting script for ComAp',
    license='GNU',
    version='1.0.0.1',

    author='Martin Rakovec',
    author_email='martinrakovec@gmail.com',

    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,

    zip_safe=False,
    install_requires=requirements,
    platforms='Platform Independent',

    scripts=['src/comap_hr_scan/rename_pdfs.py'],

    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Utilities'
    ]
)
