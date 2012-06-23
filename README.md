AnytimeEvent
============

Getting started
---------------

Install pip and virtualenv
   sudo easy\_install pip
   sudo pip install virtualenv

Create a Python virtual environment, activate it and install the requirements::

    virtualenv .
    . bin/activate
    pip install -r requirements.txt
    
Sync the database, and start up Django::

    python manage.py syncdb
    python manage.py runserver_plus
