**************
 User Manager
**************

What's this?
============
This is a **friendly** command line tool for *user management tasks* in
Linux/Unix system, which including:

* ``list`` all users and/or groups in system
* ``create``/``remove`` a user and/or group in system
* ``show``/``change`` a user's information (including *sudoer* edit)
* ``manage`` users passwd info (e.g. the Aging of password)
* et cetera (Welcome for any help and comment)

And by **friendly**, it means this tool can not only help you accomplish
your task easily, but also inform you how the task is done verbosely or
interactively. The advantages are:

* We can intuitively finish user management tasks by interacting with this
  tool directly instead of reading the lengthy and esoteric manual and
  forget afterward everytime.
* For novices of system admin tasks, this tool can also let them learn and
  understand clearly how user management work in Linux/Unix system.
* And for those SysAdmin guru, they can always switch to ``--quite`` mode and
  enjoy an unified command line interface.

Roadmap of the project
======================
The hope and destination of this project is to make this tool as default user 
management tool in Linux/Unix system. Thus a drop-in replacement for the
following tool sets: ``useradd``, ``adduser``, ``groupadd``, ``addgroup``, 
and etc.

However, at this time it's just a newborn project, any help are welcome.
You can check the stage planning and roadmap at `ROADMAP.rst`_ file.

.. _`ROADMAP.rst`: https://github.com/bingyao/usermanager/blob/master/ROADMAP.rst

License
=======
This project is released under the `MIT License`_.

.. _`MIT License`: https://opensource.org/licenses/MIT
