User guide
==========

*If you haven't installed tableD already, please follow the instruction*
:doc:`here <installation>`.

tableD has a very simple interface. This guide covers almost everything there
is to produce pretty printed tables with tableD.

To import tableD, simply put this together with your other dependencies::

    from tabled import TableD


Initializing a TableD object
----------------------------
The *TableD* object is main interface between your input data and the visual
output. The quickest way to produce a table is as follows::

    >>> TableD(['Heading 1', 'Heading 2'], [[1, 2], [3, 4]]).show()
    +-----------+-----------+
    | Heading 1 | Heading 2 |
    +-----------+-----------+
    | 1         | 2         |
    | 3         | 4         |
    +-----------+-----------+

Lets break this down. First, we initialized a TableD object with two arguments.
The first one is the headings of the table, which is a list::

    ['Heading 1', 'Heading 2']

The contents of the headings could be in any type as they would get converted
to ``str`` during table generation; The second argument is the data for the
table body, which should be a nested list of lists. Again, the input types does
not matter::

    [[1, 2], [3, 4]]

As shown in the example, the cell contents are left aligned. This is configured
by the style used, which is ``default`` by default. There are only two styles
available for now (default and terminal), but you are welcome to help create
more! You could set the style as a optional argument to the TableD object::

    TableD(<headings>, <body>, style='terminal')
