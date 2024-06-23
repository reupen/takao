Tables
======

Basic
-----

=====  =====  =======
  A      B    A and B
=====  =====  =======
False  False  False
True   False  False
False  True   False
True   True   True
=====  =====  =======

Column and row span
-------------------

+------------------------+------------+----------+----------+
| Header row, column 1   | Header 2   | Header 3 | Header 4 |
| (header rows optional) |            |          |          |
+========================+============+==========+==========+
| body row 1, column 1   | column 2   | column 3 | column 4 |
+------------------------+------------+----------+----------+
| body row 2             | Cells may span columns.          |
+------------------------+------------+---------------------+
| body row 3             | Cells may  | - Table cells       |
+------------------------+ span rows. | - contain           |
| body row 4             |            | - body elements.    |
+------------------------+------------+---------------------+

Inline code
-----------

+-----------------------+-------------------------------------------------------------------------+
| Field                 | Description                                                             |
+=======================+=========================================================================+
| ``%_display_index%``  | The current row number in the playlist view (including group headings)  |
+-----------------------+-------------------------------------------------------------------------+
| ``%_is_group% %yes%`` | Whether a group heading is currently being formatted                    |
+-----------------------+-------------------------------------------------------------------------+
| ``%_is_themed%``      | Whether ‘Themed’ has been selected as the scheme for the playlist view  |
|                       | in Colours and fonts preferences                                        |
+-----------------------+-------------------------------------------------------------------------+
