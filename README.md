# tableD: *Table for Humans*?
[![RTD badge](https://readthedocs.org/projects/tabled/badge/?version=latest)](http://tabled.readthedocs.io/en/latest/)
![MIT License badge](https://img.shields.io/badge/license-MIT-blue.svg)

Display any data in pretty printed tabular format with ease using tableD.
User guide and API documentation are available
[here](http://tabled.readthedocs.io/en/latest/).

## Usage

## Installation

## Contributing
Any contribution are welcome!
Get started by forking this repository by clicking the __*fork*__ button in
this Github page. Then clone your fork using the command line as follows:

    $ git clone https://github.com/<your_username>/tabled

Source code lives in the `/tabled` directory. To maintained good code quality,
please follow our coding convention. Documentation are generated using Sphinx
from reStructuredText format files in `/docs` as well as docstrings inlined
inside our Python modules.

[mypy](http://mypy.readthedocs.io/en/latest/index.html) is used for type
checking. Please read their documentation for more information.

### Testing:

We use pytest as our unittesting framework. Unittests lives in `/tests`
directory while doctest are inlined in python modules. To invoke all tests,
execute the following in the project's root:

    $ py.test
    
Mypy is used for type checking, you can run the checks with:
    
    $ mypy tabled/*.py tests/*.py
    
### Github Issues & Pull requests

You can post feature requests, questions and bugs in our issues tab. Please
prepend the title with appropriate tags (Feature request | Question | Bug).

Pull requests are welcome! They should be merged into the `dev` branch, only
releases are merged into the master branch to ensure its quality. Please make
sure they passed all the unittest and type checks before submitting them. 

### Workflow
We use the `rebase` workflow, which means that the history could be overwitten.
To update your local fork to upstream, do the following.

    // First time only
    $ git remote add upstream https://github.com/tommyip/tabled
    
    // Update
    $ git fetch upstream
    $ git rebase upstream/dev
