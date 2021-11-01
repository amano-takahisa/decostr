=======
decostr
=======

A package to easily decorate string output from Python to the terminal.


* Free software: MIT license


Install
--------

.. code-block:: bash

   git clone --depth 1 git@github.com:amano-takahisa/decostr.git
   pip install decostr


Usage
--------


.. code-block:: python

   from decostr.decostr import DecoStr
   s = DecoStr('underline').underline()
   print(s)
  

