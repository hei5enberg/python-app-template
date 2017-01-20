uhf-app-common
========================

This is the uhf reader application from TRFL

Usage
-----

Behavior
--------

Flexible invocation
*******************

The application can be run right from the source directory, in two different
ways:

1) Treating the readeruhf directory as a package *and* as the main script::

    $ python -m readeruhf arg1 arg2

2) Using the controlpanel-runner.py wrapper::

    $ ./app-runner.py arg1 arg2


Installation sets up bootstrap command
**************************************

Situation before installation::

    $ readeruhf
    bash: readeruhf: command not found

Installation right from the source tree (or via pip from PyPI)::

    $ python setup.py install

Now, the ``readeruhf`` command is available::

    $ readeruhf arg1 arg2


On Unix-like systems, the installation places a ``readeruhf`` script into a
centralized ``bin`` directory, which should be in your ``PATH``. On Windows,
``readeruhf.exe`` is placed into a centralized ``Scripts`` directory which
should also be in your ``PATH``.
