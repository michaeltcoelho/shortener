# Shortener

An url shortener built with Python 2.7.3 and Django 1.7.

### Requirements

* An activated virtualenv
* NodeJS

### Install Dependencies

Considering you already have enabled a virtualenv.

`$ sudo nodejs nodejs-dev npm`

If you are using a Mac OSX you can install all dependencies by HomeBrew.

### Install Shortener

Clone the repository and install it

`$ git clone https://github.com/michaeltcoelho/shortener.git`

`$ cd shortener`

`$ python setyp.py install`

### Run

Seeing you have installed all dependencies and the shortener

`$ python manage.py migrate`

`$ python manage.py runserver`