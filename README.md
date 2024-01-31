# DjangoDemo
DjangoDemo repo for EC2 

#### Setup:
- Clone git repo ```https://github.com/Mayur-Thapliyal/DjangoDemo/tree/dev``` and create a virtual python env  (recommended) by using following command:-

``` bash
python3 -m venv venv
source venv/bin/activate
```

- After creating and activating your env run:-
```bash
pip install -r requirements.txt 
python -m spacy download en_core_web_sm
```
#### Providing User details to register
- With your active python env. Redirect to DjangoDemoProj and run
```python
    python3 manage.py createsuperuser
```

- Create a user by providing required fields and remember your username and password (This will be user as your basic auth later)

#### Running auto_register
- Run
```python
python3 manage.py runserver
```
This will run your code in your localhost (127.0.0.1:8000) by default you can change the port by giveing your port no after the command 


Thank You !

Contact mail : mayurthapliyal191@gmail.com