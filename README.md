AnytimeEvent
============

Getting started
---------------

Create a Python virtual environment, activate it and install the requirements::

    virtualenv .
    . bin/activate
    pip -r requirements.txt
    
Sync the database, and start up Django::

    python manage.py syncdb
    python manage.py runserver_plus