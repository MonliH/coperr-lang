Getting Started
---------------

The page will guide you through how to run .cprr(coperr) files with the command line. You must have `the latest version of Python 3 <https://python.org>`_
and `PLY <https://www.dabeaz.com/ply/>`_ to use coperr. How to install `the latest version of Python 3 <https://python.org>`_ and `PLY <https://www.dabeaz.com/ply/>`_ will be explained in this tutorial as well.

Setup
=====

First things first, if you haven't already, get the latest version of Python. Here is the `link to their website <https://python.org>`_. You can use either Python 3.6 or Python 3.7. I would recommend Python 3.6 because coperr has not been thoroughly tested on Python 3.7 (theoretically it should work though...)

Before using coperr, you must first have `PLY <https://www.dabeaz.com/ply/>`_ installed. To install, make sure you have Python 3 in your PATH
then run:

On Windows:

``pip install ply``

On MacOS or Linux:

``pip3 install ply``

Usage
=====

To use coperr, simply run the run the coperr.py file in the command line, and pass the file you want to run as an argument.

On MacOS or Linux:

``python3 coperr.py coperr_file.cprr``

On windows, add python to your PATH then run:

``python coperr.py coperr_file.cprr``