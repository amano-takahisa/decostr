=======
tagstr
=======

A package to easily tag string output from Python to the terminal.


* Free software: MIT license


Install
--------

.. code-block:: bash

   git clone --depth 1 git@github.com:amano-takahisa/tagstr.git
   pip install tagstr


Usage
--------


.. code-block:: python

   from tagstr.tagstr import TagStr
   s = TagStr('underline').underline()
   print(s)
  

