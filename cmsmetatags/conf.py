from django.conf import settings
from django.utils.translation import gettext_lazy as _


CMSMETATAGS_FIELDSETS = getattr(
    settings,
    'CMSMETATAGS_CMSMETATAGS_FIELDSETS',
    [
        (_('Meta/Seo'), {
            'classes': ['section', 'meta-seo'],
            'fields': [
                'meta_title',
                'meta_description',
            ],
        }),
        (_('Facebook'), {
            'classes': ['section', 'facebook'],
            'fields': [
                'fb_type',
                'fb_title',
                'fb_image',
                'fb_description',
                'fb_appid',
            ],
        }),
        (_('Twitter'), {
            'classes': ['section', 'twitter'],
            'fields': [
                'tw_title',
                'tw_image',
                'tw_description',
            ],
        }),
    ]
)


FB_IMAGE_OPTIONS = getattr(
    settings,
    'CMSMETATAGS_FB_IMAGE_OPTIONS',
    {
        'size': (1200, 1200),
        'crop': False,
        'quality': 95
    }
)
FB_IMAGE_DEFAULT_PATH = getattr(
    settings,
    'CMSMETATAGS_FB_IMAGE_DEFAULT_PATH',
    ''
)

TW_IMAGE_OPTIONS = getattr(
    settings,
    'CMSMETATAGS_TW_IMAGE_OPTIONS',
    {
        'size': (1200, 1200),
        'crop': False,
        'quality': 95
    }
)
TW_IMAGE_DEFAULT_PATH = getattr(
    settings,
    'CMSMETATAGS_TW_IMAGE_DEFAULT_PATH',
    ''
)


PROTOCOL = getattr(
    settings,
    'CMSMETATAGS_PROTOCOL',
    'https'
)
