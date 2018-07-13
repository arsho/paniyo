python3 -m virtualenv venv --no-site-packages
source venv/bin/activate
pip install django
pip freeze>requirements.txt

django-admin startproject paniyosite
paniyo cd paniyosite
python manage.py startapp product_information


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'paniyo_db',
        'USER': 'paniyo',
        'PASSWORD': '123',
        'HOST': '172.17.0.6',
        'PORT': '3306'
    }
}

#### MySQL openshift application information
- Memory Limit: 200Mi
- Namespace: openshift
- Database service name: mysql
- MySQL connection username: paniyo
- MySQL connection password: 123
- MySQL root user password: 123
- MySQL Database name: paniyo_db
- Volume Capacity: 400Mi
- Version of MySQL image: 5.7
- Labels:
    - template: mysql-persistent-template: 
    - app: mysql-persistent
    
```
The following service(s) have been created in your project: mysql.

       Username: paniyo
       Password: 123
  Database Name: paniyo_db
 Connection URL: mysql://mysql:3306/
```

#### Make commands
- make migrations
- make migrate
- make run
