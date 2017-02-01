============================
tableD: *Tables for Humans?*
============================

v0.1.0 (`Github`_)

**tableD** pretty prints your data in a tabular format. With its clean and
simple API, you can generate fancy tables in no time! And did I mention it is
extremely flexible and configurable?

Quick start::

    >>> headings = ['x', 'f(x) = x^2', 'f(x) = x^x']
    >>> data = [[x, x**2, x**x] for x in range(1, 11)]

    # Generate table!
    >>> tabled.new(headings, data, style='terminal').show()
    ╔════╦════════════╦═════════════╗
    ║ x  ║ f(x) = x^2 ║ f(x) = x^x  ║
    ╠════╬════════════╬═════════════╣
    ║ 1  ║ 1          ║ 1           ║
    ║ 2  ║ 4          ║ 4           ║
    ║ 3  ║ 9          ║ 27          ║
    ║ 4  ║ 16         ║ 256         ║
    ║ 5  ║ 25         ║ 3125        ║
    ║ 6  ║ 36         ║ 46656       ║
    ║ 7  ║ 49         ║ 823543      ║
    ║ 8  ║ 64         ║ 16777216    ║
    ║ 9  ║ 81         ║ 387420489   ║
    ║ 10 ║ 100        ║ 10000000000 ║
    ╚════╩════════════╩═════════════╝

Table Of Contents
-----------------

.. toctree::
    :maxdepth: 3

    installation
    user_guide
    api_documentation
    contributors_guide

.. _Github: https://github.com/tommyip/tabled
