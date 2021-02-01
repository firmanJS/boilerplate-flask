# Boilerplate-Flask
[![Maintainability](https://api.codeclimate.com/v1/badges/ef9029f8c10ed08f7c56/maintainability)](https://codeclimate.com/github/firmanJS/boilerplate-flask/maintainability)

## About

This is api service boilerplate example


## Installation

If you are using **windows**,

First include the python to venv

```
py -3 -m venv venv
```

And activate the venv

```
venv\Scripts\activate
pip install -r requirement.txt
```


If you are using **linux**,

First install venv

```sh
sudo apt-get install python3-pip
sudo pip3 install virtualenv 
```

include the python to venv

```
virtualenv -p python3.x venv
```

And activate the venv

```
source venv/bin/activate
pip install -r requirement.txt
```

example install package
```sh
pip install package && pip freeze > requirements.txt
```

migrate table
```sh
$ flask db init
$ flask db migrate
$ flask db upgrade
```

# Usage

Run the script

```
python run.py
```

You can see which port the api server running
