import os

from setuptools import setup

setup(
    name="vboxapi",
    version=os.environ.get("VBOX_VERSION", '4.3.10'),
    description="Python interface to VirtualBox",

    url='http://www.virtualbox.org',

    # Author details
    author='Oracle Corp.',

    # Choose your license
    license='GPLv2',

    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4'
    ],

    packages=['vboxapi']
)
