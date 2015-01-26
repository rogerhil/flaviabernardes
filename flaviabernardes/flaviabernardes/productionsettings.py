

ADMINS = (
    ('Rogerio Hilbert', 'rogerhil@gmail.com')
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'flaviabernardes',
        'USER': 'rogerhil_flaviabernardes',
        'PASSWORD': 'Natasha1',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}


STATIC_ROOT = '/home/rogerhil/webapps/flaviabernardes_static_media/'

STATICFILES_DIRS = (
    '/home/rogerhil/webapps/flaviabernardes/flaviabernardes/flaviabernardes/media',
    '/home/rogerhil/webapps/flaviabernardes/flaviabernardes/flaviabernardes/static'
)
