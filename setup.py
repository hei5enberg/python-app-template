# -*- coding: utf-8 -*-

"""setup.py: setuptools control."""

import re
from setuptools import setup


version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('readeruhf/app.py').read(),
    re.M
    ).group(1)


with open("README.rst", "rb") as f:
    long_descr = f.read().decode("utf-8")


setup(
    name = "uhf-app-common",
    packages = ["readeruhf"],
    entry_points = {
        "console_scripts": [
            'readeruhf = readeruhf.app:main',
            'reader-monitor = readeruhf.app_monitor:main',
            'reader-deletelogs = readeruhf.deletelogs:main',
            'reader-resend = readeruhf.resend:main',
            'reader-network = readeruhf.con_monitor:main'
            ]
        },
    version = version,
    description = "Ultra High Frequency Reader dev program",
    long_description = long_descr,
    install_requires=[
        'config',
        'requests',
        'tornado',
    ],
    data_files=[
        ('/etc/', ['uhfdata.cfg']),
        ('/home/pi/', ['lib/libR2000_SDK.so']),
        ('/home/pi/', ['lib/libR2000_SDKS.so']),
        ('/usr/lib/', ['lib/librfidtx.so']),
        ('/usr/lib/', ['lib/libcpl.so']),
        ('/usr/lib/', ['lib/librfid.so'])
        ],
    author = "Abhijith Soman",
    author_email = "abhijiths@trackrf.com",
    )

    #   data_files=[('bitmaps', ['bm/b1.gif', 'bm/b2.gif']),
    #               ('config', ['cfg/data.cfg']),
    #               ('/etc/init.d', ['init-script'])]
# setup(
#     name='uhf-app-common',
#     version='0.1',
#     py_modules=['yourscript'],
#     install_requires=[
#         'Click',
#     ],
#     entry_points='''
#         [console_scripts]
#         uhfreader=uhfreader:main
#     ''',
# )
