# Employee directory

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/rustamrv/company.git
$ cd company
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python3 -m venv env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip3 install -r requirements.txt 
(env)$ python3 data.py
(env)$ python3 manage.py runserver
And navigate to `http://127.0.0.1:8000/`.
```
 
[Task description](https://github.com/rustamrv/company/blob/master/task.pdf)


<object data="task.pdf" type="application/pdf" width="100%"> 
</object>