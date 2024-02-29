This is a repeatable example for a bug I found in sphinx viewcode, which causes an IndexError(list index out of range) when a child module's file is shorter than the parent module's file.

To build the repeatable example, run the following commands:

clone the repo,
build the python environment, conda (see either env.txt or environment.yml),

.. code-block::

        cd ../docs_build
        make html


To fix it, just add some extra lines to the child module's file (blank lines in the header for instance), or remove some lines from the parent module's file.