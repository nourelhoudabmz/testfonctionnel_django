# Backend Setup
## Prerequisites


* Ubuntu / MAC Preferred
* Python 3.8.5
* Django 3.1.5
* SQLite3

### Environment Setup.
    sudo apt-get update
    sudo apt install python3-venv
    python3 -m venv venv
    source venv/bin/activate

#### Install Requirements

```pip install -r requirments.txt```

### Migrate
 Migrate the models with command
 ```python3 manage.py migrate```
 
### Run the server
Run the django server with command
```python3 manage.py runserver```

### Create a Superuser to access Admin Panel
Run the management command to create superuser
```python3 manage.py createsuperuser```

To get the admin login page, type in url bar:
```http://127.0.0.1:8000/admin/ ```

Now the server should be up and running on http://127.0.0.1:8000