from __future__ import unicode_literals

from django import forms
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase


from .. import conf
from ..models import CMSMetaTags


class CMSMetaTagsPluginForm(forms.ModelForm):

    class Meta:
        fields = '__all__'
        model = CMSMetaTags
        labels = {}
        widgets = {}


class CMSMetaTagsPlugin(CMSPluginBase):

    allow_children = False
    fieldsets = conf.CMSMETATAGS_FIELDSETS
    form = CMSMetaTagsPluginForm
    model = CMSMetaTags
    module = _('Meta/SEO')
    name = _('Meta/SEO Tags')
    render_template = 'metatags/plugin_metatags.html'

    def render(self, context, instance, placeholder):
        context.update({
            'object': instance,
            'placeholder': placeholder,
            'fb_image_url': self.get_fb_image_url(
                context.get('request'),
                instance,
            ),
        })
        return context

    def get_fb_image_url(self, request, obj):
        path = None
        img = obj.get_fb_image()
        if img:
            path = img.url
        elif conf.FB_IMAGE_DEFAULT_PATH:
            path = conf.FB_IMAGE_DEFAULT_PATH
        if path:
            site = Site.objects.get_current(request=request)
            return '{}://{}{}'.format(conf.PROTOCOL, site.domain, path)
        return ''
