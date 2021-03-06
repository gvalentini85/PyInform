Getting Started
===============

Pip Installation
----------------

PyInform is installable under **Linux**, **OS X** and **Windows** via pip. To
install, all you have to do is ::

    $ pip install pyinform

If you don't already have `NumPy`_ installed, you can either install it manually
via ::

    $ pip install numpy
    
or use the ``REQUIREMENTS.txt`` provided in the PyInform git repo::

    $ pip install -r REQUIREMENTS.txt

PyInform is continuously tested on **Linux** and **Windows** via `Travis-CI`_
and `AppVeyor`_ respectively, and used regularly on **OS X** by the
maintainers. Python version 2.7, 3.4 and 3.5 are supported.

.. _NumPy: http://www.numpy.org/
.. _Travis-CI: https://travis-ci.org/ELIFE-ASU/PyInform
.. _AppVeyor: https://ci.appveyor.com/project/dglmoore/pyinform-i8m0b

Installation from Source
------------------------

If you are interested in installing from source, we recommend using pip. First
clone down the repo and within the project root run ::

    $ pip install .
    
You might have to use ``sudo`` depending on your environment. This will result
in a system-wide installation. If you want to install for your account only, or
if you don't have ``sudo`` privileges on your machine ::

    $ pip install --user .
    
Using this installation method, PyInform can be installed in "editable" mode, 
meaning that changes made to the repo's source will automatically be made
available throughout. To install in "editable" mode, ::

    $ pip install --editable .
    
(with or without --user).