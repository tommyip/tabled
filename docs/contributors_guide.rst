Contributors guide
==================

Contributions are welcome! Before you submit a pull requests, please read the
following guide to make sure your changes are ready to be merged into the
code base.

Version control
---------------

Quick start guide
^^^^^^^^^^^^^^^^^
We use **Git** as our version control system, you should have the following
in mind when working on TableD:

1. We use a **rebase** workflow in order have to clean Git history. To update
   your local branch to the latest source tree, execute the following in your
   terminal::

       // Set tommyip/tabled remote (FIRST TIME ONLY)
       $ git remote add upstream https://github.com/tommyip/tabled

       $ git pull --rebase upstream master

2. To have your pull requests merged as quickly as possible, please resolve all
   merge conflict and make sure your changes passed the test suite before
   submitting them.

Using Git & Github in tableD
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Commits
"""""""
Commits should have a short title clearly stating the purpose of the changes.
You should also prepend the title with one of the following section headings
to make future maintance easier:

* ``code``: New feature
* ``refactor``: Code refactoring
* ``docs``: Documentation
* ``deps``: Dependency
* ``setup``: Project setup

Each commit should have a single purpose. Commits with modification to
multiple areas of the codebase are not encouraged and will not be merged.
If in doubt, just have a look at our Git history.

Testing
-------

You can invoke the test suite with ``make test`` in the root directory. The
following would be executed in the process:

1. pytest - Unit testing framework
2. mypy - Static type checking
3. flake8 - Source code linter

A coverage report would also be produced by pytest. We have a 100% test
coverage and we would like to maintain that; when you make changes to the
source code, please check if modifying or adding new tests are necessary.
