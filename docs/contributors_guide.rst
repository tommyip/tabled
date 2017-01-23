Contributors guide
==================

Contributions are welcome! Before you submit a pull requests, please read the
following guide to make sure your commits are ready to merge into our code
base.

Version control
---------------

Quick start guide
^^^^^^^^^^^^^^^^^
We use **Git** as our version control system. If you are unfamiliar with Git,
we encourage you to first read their documentation. Those who have used Git
before should have the following in mind when contributing to tableD:

1. We use a **rebase** workflow in order to have a cleaner history. To update
   your local branch to the latest source tree, execute the following in your
   terminal::

       // First time only
       $ git remote add upstream https://github.com/tommyip/tabled

       // Update local repository to match master
       $ git fetch upstream && git rebase upstream/master

2. To have your pull requests merged as quickly as possible, please resolve all
   merge conflict and make sure your changes passed the test suite before
   submitting them.

Using Git & Github in tableD
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Commits
"""""""
Commits should have a short title in the first line clealy stating the purpose
of the changes. Choose one of the following and prepend them to the title of a
commit:

* ``code``: New code
* ``refactor``: Code refactoring
* ``docs``: Documentation
* ``deps``: Dependency
* ``setup``: Project setup

Each commit should have a single purpose. A commit with modification to
multiple modules and areas are hard to review and defeat the purpose of a
version control system. Here are a few examples::

    // Good:
    code: Add `device` attribute to the tabled.TableD object.

    The `device` attribute determines how should the table
    be presented to the user.

    // Bad:
    - New feature
    - Change docs
    - Remove module

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
