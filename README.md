# Shortener

An url shortener built with Python 2.7.6 and Django 1.7.

### Requirements

* An activated python virtualenv.
* NodeJS.

### Install Dependencies

If you are using Linux:

You can find a tutorial about how to setup a python virtualenv on linux [here](https://wiki.archlinux.org/index.php/Python_VirtualEnv).

To install NodeJS run:

`sudo apt-get install nodejs npm`

If you are using a Mac OSX, you can install the dependencies by [HomeBrew](http://brew.sh/):

You can find a tutorial about how to setup a python virtualenv on Mac OSX [here](http://jamie.curle.io/blog/installing-pip-virtualenv-and-virtualenvwrapper-on-os-x/)

To install NodeJS run:

`brew install node`

####Considering you already have installed the dependencies, created and activated your virtualenv:

### Install Shortener

Clone the repository and install it:

`$ git clone https://github.com/michaeltcoelho/shortener.git`

Go to `/shortener` directory:

`cd shortener`

Run the following command:

`make install`

### Test

Running tests:

`make test`

### Run

Running the application:

`make run`