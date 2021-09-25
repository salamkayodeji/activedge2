Exercise 3
===================================

Installation
------------

Once unzipped, follow the installation guides below.

### Installation in Windows

* Download and install [Python](https://www.python.org/downloads/). For this
  guide, we assume Python is installed in `C:\Python36`.
* Download the Pip (Python package installer) bootstrap script
  [get-pip.py](https://bootstrap.pypa.io/get-pip.py).
* In the command prompt, run `C:\Python36\python.exe get-pip.py` to install
  `pip`.
* In the command prompt, run `C:\Python36\scripts\pip install virtualenv` to
  install `virtualenv`.

### Installation in Ubuntu

Python 3 is preinstalled in Ubuntu. Virtualenv and pip necessarily aren't, so:

* `sudo apt-get install python-virtualenv python-pip`

### Creating and activating a virtualenv

Go to the project root directory and run:

Windows:

```
c:\location_of_project>c:\Python35\scripts\virtualenv --system-site-packages venv
c:\location_of_project>venv\Scripts\activate
```

Ubuntu:

```
virtualenv -p /usr/bin/python3 --system-site-packages venv

for python 3.9

python -m venv "virtual env name"

source venv/bin/activate
```

Starting the project
--------------------

After activating the virtualenv do the following

```
cd app
pip install -r requirements.txt
python manage.py migrate 
python manage.py runserver
```

Now the test should be visible in the browser at
[`http://127.0.0.1:8000/`](http://127.0.0.1:8000/).

GET /api/stocks (get a list of stocks) : http://127.0.0.1:8000/api/stocks
GET /api/stocks/1 (get one stock from the list) : http://127.0.0.1:8000/api/stocks/1
PUT /api/stocks/1 (update the price of a single stock) : http://127.0.0.1:8000/api/stocks/1
POST /api/stocks (create a stock): http://127.0.0.1:8000/api/stocks