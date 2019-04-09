# DJANGO CMSMetaTags

!!! ALPHA !!!  

## configure

settings.py:
```python
INSTALLED_APPS = [
    '...',
    'cmsmetatags',
    '...'
]
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
```

## Plugins

* CMSMetaTagsPlugin

## Important
Make sure the placeholder you allow metatags in, comes after the cms render_block tags  
```html
<head>
    <meta charset="utf-8">
    {% render_block 'css' %}{% render_block 'js' %}
    {% placeholder 'metatags' %}
</head>
```