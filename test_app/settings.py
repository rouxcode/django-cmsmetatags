import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '0_h78ag(pr0_-7_l-yi3+__9nk2*uu!qrd$iju*h6^sghuj!g@'
SITE_ID = 1
DEBUG = True
TIME_ZONE = 'Europe/Zurich'
USE_TZ = True
USE_I18N = True
USE_L10N = True
LANGUAGE_CODE = 'en'
LANGUAGES = [
    ('de', 'Deutsch'),
    ('en', 'English'),
    ('fr', 'French'),
]


ALLOWED_HOSTS = [
    '127.0.0.1',
]
ADMINS = (
    ('admin', 'info@rouxcode.ch'),
)
MANAGERS = (
    ('admin', 'info@rouxcode.ch'),
)


WSGI_APPLICATION = 'test_app.wsgi.application'
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STORAGE_ROOT = os.path.join(BASE_DIR, 'storage')
STATIC_ROOT = os.path.join(STORAGE_ROOT, 'test_app', 'static')
MEDIA_ROOT = os.path.join(STORAGE_ROOT, 'media')


INSTALLED_APPS = [
    'test_app',
    'cmsmetatags',

    'cms',
    'menus',
    'treebeard',
    'sekizai',

    'filer',
    'mptt',
    'polymorphic',
    'easy_thumbnails',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.redirects',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
]

MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.utils.ApphookReloadMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
]

ROOT_URLCONF = 'test_app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'test_app', 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.template.context_processors.csrf',
                'django.template.context_processors.tz',
                'django.template.context_processors.static',
                'sekizai.context_processors.sekizai',
                'cms.context_processors.cms_settings'
            ],
        },
    },
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'test_app', 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'}, # NOQA
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'}, # NOQA
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'}, # NOQA
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'}, # NOQA
]

CMS_TEMPLATES = (
    ('base.html', 'Default'),
)
CMS_PLACEHOLDER_CONF = {
    'metatags': {
        'name': 'Meta/SEO tags',
        'plugins': [
            'CMSMetaTagsPlugin',
        ],
        'default_plugins': [
            {
                'plugin_type': 'CMSMetaTagsPlugin',
                'values': {},
            },
        ],
        'limits': {
            'CMSMetaTagsPlugin': 1,
        },
    },
}
CMS_PERMISSION = False
CMS_CACHE_DURATIONS = {
    'content': 0,
    'menus': 0,
    'permissions': 0,
}
CMS_LANGUAGES = {
    1: [
        {
            'code': 'de',
            'name': 'Deutsch',
            'fallbacks': ['fr'],
        },
        {
            'code': 'en',
            'name': 'English',
            'fallbacks': ['de'],
        },
        {
            'code': 'fr',
            'name': 'French',
            'fallbacks': ['de'],
        },

    ],
    'default': {
        'fallbacks': ['de', 'fr', 'en'],
        'redirect_on_fallback': True,
        'public': True,
        'hide_untranslated': True,
    },
}
CMS_MENU_TITLE_OVERWRITE = True
CMS_REDIRECTS = True
CMS_URL_OVERWRITE = False


CMSMETATAGS_FB_IMAGE_DEFAULT_PATH = '{}default.png'.format(STATIC_URL)
