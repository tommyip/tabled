==================
Contributors guide
==================

Contributions are welcome! Before you submit a pull requests, please read the
following guide to make sure your commits are ready to merge into our code
base.

---------------
Version control
---------------

Quick start guide
^^^^^^^^^^^^^^^^^
We use **Git** as our version control system. If you are unfamiliar with Git,
we encourage you to first read their documentation. An excellent one is
available over at `git-scm`_. Those who have used Git before should have the
following in mind when contributing to tableD.

1. We use a rebase workflow in order to have a cleaner history. To update
   your local branch to the latest master source tree, execute the following
   in a terminal::

       // First time only
       $ git remote add upstream https://github.com/tommyip/tabled

       // Update local repository to match master
       $ git fetch upstream && git rebase upstream/master

2. Code reviews are done directly in Github. To have your pull requests merged
   as quick as possible, please resolve all merge conflict and make sure all
   the available tests passed before submitting them.

Using Git & Github in tableD
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Commits
"""""""
Commits should have a short title in the first line clealy stating the purpose
of the changes. You should prepend the title with one of the following
categories:

* ``code``: Code
* ``docs``: Documentation
* ``deps``: Dependency
* ``setup``: Project setup

Long commit messages are not necessary unless your changes are not obvious.
Here are a few examples::

    // Good:
    code: Add `device` attribute to the tabled.TableD object.

    The `device` attribute determines how should the table
    be presented to the user.

    // Bad:
    New code to tabled

    Added new code to application. This should make the
    table look better.


-------
Testing
-------

An extensive suite of unittests are written to prevent any bugs and regressions
from introducing. Our main unittesting framework is `pytest`_. You can invoke
these tests with ``py.test`` in the root directory.


.. _git-scm: https://git-scm.com/doc
.. _pytest: http://doc.pytest.org/
