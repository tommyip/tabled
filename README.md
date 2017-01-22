<p align="center">
    <img src="docs/.static/logo.png" alt="tableD" width="50%" height="50%">
</p>
<p align="center">
    <a href="https://travis-ci.org/tommyip/tabled">
        <img src="https://travis-ci.org/tommyip/tabled.svg?branch=master" alt="Tavis CI">
    </a>
    <a href="https://coveralls.io/github/tommyip/tabled?branch=master">
        <img src="https://coveralls.io/repos/github/tommyip/tabled/badge.svg?branch=master" alt="Coveralls">
    </a>
    <a href="http://tabled.readthedocs.io/en/latest/?badge=latest">
        <img src="https://readthedocs.org/projects/tabled/badge/?version=latest" alt="Read The Docs">
    </a>
    <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="MIT license">
</p>

# tableD: *Tables for Humans?*

**tableD** pretty prints your data in a tabular format. With its clean and
simple API, you can generate fancy tables in no time! And did I mention it is
extremely flexible and configurable?

Quick start:
```.py
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
```

Detailed documentation is available over at [Read the Docs][docs].

[docs]: http://tabled.readthedocs.io/en/latest/
