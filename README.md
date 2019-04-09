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
```

## Plugins

* CMSMetaTagsPlugin


```html
{% load cmslogin_tags %}
<head>
    <meta charset="utf-8">
    {% render_block 'css' %}{% render_block 'js' %}
    {% placeholder 'metatags' %}
</head>
```