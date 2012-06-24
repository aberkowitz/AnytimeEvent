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
    
Copy the local_settings.py.template -> local_settings.py and add email password::

    cd anytimeevent
    cp local_settings.py.template local_settings.py
    
Sync the database, and start up Django::

    python manage.py syncdb
    python manage.py collectstatic
    python manage.py runserver_plus


Credits
-------

- CSS3 social media icons thanks to http://nicolasgallagher.com/lab/css3-social-signin-buttons/
