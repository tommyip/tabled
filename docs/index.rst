============================
tableD: *Tables for Humans?*
============================

v0.1.0 (`Github`_)

**tableD** pretty prints your data in a tabular format. With its clean and
simple API, you can generate fancy tables in no time! And did I mention it is
extremely flexible and configurable?

Quick start::

    >>> headings = ['x', 'f(x) = x^2', 'f(x) = x^3']
    >>> data = [[x, x ** 2, x ** 3] for x in range(1, 6)]

    # Generate table!
    >>> TableD(headings, data, style='terminal').show()
    ╔═══╦════════════╦════════════╗
    ║ x ║ f(x) = x^2 ║ f(x) = x^3 ║
    ╠═══╬════════════╬════════════╣
    ║ 1 ║ 1          ║ 1          ║
    ║ 2 ║ 4          ║ 8          ║
    ║ 3 ║ 9          ║ 27         ║
    ║ 4 ║ 16         ║ 64         ║
    ║ 5 ║ 25         ║ 125        ║
    ╚═══╩════════════╩════════════╝

.. toctree::
   :maxdepth: 3

   installation
   user_guide
   api_documentation
   contributors_guide

.. _Github: https://github.com/tommyip/tabled
