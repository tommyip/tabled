User guide
==========

*If you haven't installed tableD already, please follow the instruction*
:doc:`here <installation>`.

Creating a new table
--------------------

First, import the tabled package::

    import tabled

The *TableD* object is the main interface for visualizing your data, you can
create a new instance using the new constructor function::

    >>> tabled.new(['Heading 1', 'Heading 2'],
    ...            [[1, 2], [3, 4]]).show()
    +-----------+-----------+
    | Heading 1 | Heading 2 |
    +-----------+-----------+
    | 1         | 2         |
    | 3         | 4         |
    +-----------+-----------+

Lets break this down. The new function creates and returns a TableD object,
which accepts 4 optional arguments.

Headings
""""""""

The heading argument should be a list of elements, the type of the cell
would be converted to string automatically. Examples::

    ['Heading 1', 'Heading 2', some_variable, 10, True]

    [x for x in range(10)]  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

Data
""""

The second argument, data, is a nested list of lists containing the table
body. Same as the headings, each cell element could be in any Python types.
Examples::

    [[1, 2], [3, 4], ["Cell 5", 6], [True, False]]

    [[x, x+1] for x in range(3)]  # [[0, 1], [1, 2], [2, 3]]

Style
"""""

The style of the table is configured through the style argument, which is
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

Align
"""""

By default, the style template already provides an alignment setting, but it is
possible to customize it using this argument. The available alignments are
**left**, **center** and **right**::

    >>> tabled.new(['Heading 1', 'Heading 2'], [[1, 2], [3, 4]],
    ...            align='right').show()
    +-----------+-----------+
    | Heading 1 | Heading 2 |
    +-----------+-----------+
    |         1 |         2 |
    |         3 |         4 |
    +-----------+-----------+

Device
""""""

The device argument controls where the output is shown. The default is stdout,
which is your terminal or python shell.

*More device options are coming soon...*

Displaying the table
--------------------

The ``.show()`` method displays your table to standard output by default. It
supports caching, so it would rerender your data only if they were modified.

Modification after initialization
---------------------------------

The arguments to ``tabled.new()`` are optional as mentioned above, they could
be added or changed after the initialization of a new tabled instance. Here are
the available setter methods, which are fairly self explanatory::


    >>> t = tabled.new()

    # Set the table headings
    >>> t.set_headings(['Language', 'Typing', 'Runtime', 'Type'])

    # Add a new row to the bottom of the table
    >>> t.add_row(['Python', 'Dynamic', 'CPython', 'OOP'])

    # Add multiple rows to the table (must be nested list)
    >>> t.add_rows([
        ['Java', 'Static', 'JVM', 'OOP'],
        ['Elixir', 'Dynamic', 'BEAM', 'Functional']
    ])

.. note:: The number of columns of your table is determined by the headings.
          If any of your rows is shorter than the headings, blank cells would
          be appended to the end of the row.

If you now display the table, you will get::

    >>> t.show()
    +----------+---------+---------+------------+
    | Language | Typing  | Runtime | Type       |
    +----------+---------+---------+------------+
    | Python   | Dynamic | CPython | OOP        |
    | Java     | Static  | JVM     | OOP        |
    | Elixir   | Dynamic | BEAM    | Functional |
    +----------+---------+---------+------------+
