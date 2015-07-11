from __future__ import absolute_import

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os, re


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT = re.sub(r'/annuts_server/?$', '/', os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5u5ve^8jvee-uy3yitiz=jwdasi6wn&@ngio%@yyy$a9976!-5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

#qiqiu
QINIU_ACCESS_KEY = 'LmFtUSlKIF8p0briHvAv0S07oT3Xlodp2Wga71_C'
QINIU_SECRET_KEY = 'yH9efgzEhaXLDOnZ7D1UYckf0pmUgKDJwkel-3hm'

#jpush
JPUSH_APP_KEY = '2be0e84d47c236b4f579e208'
JPUSH_MASTER_SECRET = '77271a9d92565359e7508fc3'

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'annuts_app',
    'rest_framework',
    'api',
    #'kombu.transport.django.KombuAppConfig',
    'dashboard'
)

# Celery settings

CELERY_IMPORTS = ('annuts_app.tasks.an_push')

BROKER_URL = 'redis://localhost:6379/0'

#: Only add pickle to this list if your broker is secured
#: from unwanted access (see userguide/security.html)
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny'
    ]
}


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'annuts_server.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(ROOT, 'templates'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'annuts_server.wsgi.application'

AUTH_PROFILE_MODULE = 'annuts_app.UserProfile'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'annuts',
	'USER': 'root',
	'PASSWORD': 'annuts',
	'HOST': 'localhost',
	'PORT': '3306'
    }
}

CELERY_REDIS_HOST = "localhost"

BROKER_URL = "redis://%s:6379/2" % CELERY_REDIS_HOST


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(ROOT, 'static'),
)

print os.path.join(ROOT, 'static')
