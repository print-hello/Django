import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8(eo3ox45g^b%t^$$z1*#xrxio&h*u6(+p$tgw0a-towb-1u99'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'menu',
    'pinBigAccount',
    'pinSmallAccount',
    'pinBabyAccount',
    'storenvy',
    'pinBusinessAccount',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'accountMonitor.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            # os.path.join(BASE_DIR, 'static')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'menu.views.global_params',
            ],
        },
    },
]

WSGI_APPLICATION = 'accountMonitor.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pin_login_system',
        "USER": "root",
        "PASSWORD": "123456",
        "HOST": "localhost",
        "PORT": "3306",
    },
    'pin_login_system': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pin_login_system',
        "USER": "root",
        "PASSWORD": "123456",
        "HOST": "localhost",
        "PORT": "3306",
    },
    'pinterest': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pinterest',
        "USER": "root",
        "PASSWORD": "Hbjjz7r9ptyefzjv48ur2",
        "HOST": "107.150.61.250",
        "PORT": "3306",
    },
    'new_pin': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'new_pin',
        "USER": "root",
        "PASSWORD": "Hbjjz7r9ptyefzjv48ur2",
        "HOST": "107.150.61.250",
        "PORT": "3306",
    },
    'storenvy': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'storenvy',
        "USER": "root",
        "PASSWORD": "123456",
        "HOST": "localhost",
        "PORT": "3306",
    },
    'pin_data_crawl': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pin_data_crawl',
        "USER": "root",
        "PASSWORD": "123456",
        "HOST": "localhost",
        "PORT": "3306",
    },
}

DATABASE_ROUTERS = ['accountMonitor.database_router.DatabaseAppsRouter']

DATABASE_APPS_MAPPING = {
    'pinBigAccount': 'pin_login_system',
    'pinSmallAccount': 'pinterest',
    'pinBabyAccount': 'new_pin',
    'pinBusinessAccount': 'pin_data_crawl',
    'storenvy': 'storenvy',
    'admin': 'pin_login_system',
    'auth': 'pin_login_system',
    'contenttypes': 'pin_login_system',
    'sessions': 'pin_login_system',
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'
if DEBUG:
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static'),
    ]
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
