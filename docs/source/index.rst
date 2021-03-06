.. coperr documentation master file, created by
   Jonathan Li. 2019.

Welcome to Coperr's Documentation!
==================================

This is the official documentation for `coperr-lang <https://github.com/MonliH/coperr-lang>`_.
Coperr is a dynamically typed programming language implemented in `Python 3 <https://www.python.org/>`_.
It is inspired by C++, C, Java, and mainly Python. Coperr uses a LALR\(1\) parser to parse its grammar.
Coperr is an interpreted language (for now...).

Design Principles
^^^^^^^^^^^^^^^^^

- **Be easy to read.** Copper has been designed to be easy to read, and easy to learn.
  It is similar to Python 3, making it easier to learn for those who know the language. It also does not use newlines (`Off-side Rule <https://en.wikipedia.org/wiki/Off-side_rule>`_)
  which makes it easier to learn for people coming from languages like C and C++.

- **Be faster then Python 3.** Coperr has a pure python implementation, which means you can use modules like `Pypy <https://pypy.org/>`_ and `CPython <https://github.com/python/cpython>`_.
  Use of Pypy or CPython can possibly make it even faster the normal Python 3 (even though it is written in Python 3).

- **Have a consistent syntax.** Copper's syntax was designed to be elegant and consistent. It does **not** have many exceptions/inconsistencies as far as syntax is concerned.

- **Be different.** You might be thinking, why would I ever use this over Python (or some other programming language)?
  It's just another language to learn, and it provides the same features as a lot of other programming languages.
  That's where your wrong. I am is currently implementing a powerful new programming paradigm that will boost your productivity and make your want to use Coperr!

Contents
^^^^^^^^

.. toctree::
   :maxdepth: 3

   getting_started
   examples
   license
   features
   todo

.. * :ref:`genindex`
.. * :ref:`modindex`

* :ref:`search`
