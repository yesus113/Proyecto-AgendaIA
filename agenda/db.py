import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

POSTGRESQL = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'agenda',
        'USER': 'postgres',
        'PASSWORD': 'emma2002',
        'HOST': 'localhost',
        'PORT': '5432',

    }

}