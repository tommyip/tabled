User guide
==========

*If you haven't installed tableD already, please follow the instruction*
:doc:`here <installation>`.

tableD has a very simple interface. This guide covers almost everything there
is to produce pretty printed tables with tableD.

Importing tabled is as simple as::

    import tabled

Creating a new table
--------------------
The *TableD* object is the main interface for visualizing your data. You can
create a tabled object using the ``new`` function and ``show`` to display it
to standard output::

    >>> tabled.new(['Heading 1', 'Heading 2'],
                   [[1, 2], [3, 4]]).show()
    +-----------+-----------+
    | Heading 1 | Heading 2 |
    +-----------+-----------+
    | 1         | 2         |
    | 3         | 4         |
    +-----------+-----------+

Lets break this down. The ``new`` function creates and returns a TableD object,
it accepts a list of headings, a nested lists of cell data, the style of the
output and device to be outputted to.

Headings
""""""""

The ``heading`` argument should be a list of elements, which could be in any
Python type. Examples::

    ['Heading 1', 'Heading 2', some_variable, 10, True]

    [x for x in range(10)]  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

Data
""""

The second argument, ``data``, is a nested list of lists containing cell data
for the table body. Same as the headings, each cell element could be in any
Python types. Examples::

    [[1, 2], [3, 4], ["Cell 5", 6], [True, False]]

    [[x, x+1] for x in range(3)]  # [[0, 1], [1, 2], [2, 3]]

Style
"""""

The style of the table is configured through the ``style`` argument, which is
*default* for default. There are only two styles available for now, but you
are welcome to help create more, see
:doc:`Contributors Guide<contributors_guide>` for more information.

.. code-block:: python

    headings = ['x', 'y1', 'y2']
    data = [[x, x*x, x**3] for x in range(3)]

Default::

    >>> tabled.new(headings, data).show()
    +---+----+----+
    | x | y1 | y2 |
    +---+----+----+
    | 0 | 0  | 0  |
    | 1 | 1  | 1  |
    | 2 | 4  | 8  |
    +---+----+----+

Terminal::

    >>> tabled.new(headings, data, style='terminal').show()
    ╔═══╦════╦════╗
    ║ x ║ y1 ║ y2 ║
    ╠═══╬════╬════╣
    ║ 0 ║ 0  ║ 0  ║
    ║ 1 ║ 1  ║ 1  ║
    ║ 2 ║ 4  ║ 8  ║
    ╚═══╩════╩════╝

Device
""""""

The ``device`` argument controls where the output is shown. The default is
``stdout``, which is your terminal or python shell.

*More device options are coming soon...*
