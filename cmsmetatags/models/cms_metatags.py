from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin
from easy_thumbnails.files import get_thumbnailer
from filer.fields.image import FilerImageField

from .. import conf


"""
https://developers.facebook.com/docs/sharing/webmasters
"""


class CMSMetaTags(CMSPlugin):

    meta_title = models.CharField(
        max_length=255,
        default='',
        blank=True,
        verbose_name=_('Page title'),
        help_text=_(
            'shown as browser tab title, defaults to page->settings->title'
        )
    )
    meta_description = models.TextField(
        max_length=355,
        blank=True,
        default='',
        verbose_name=_('Meta description'),
        help_text=_(
            'SEO descriptiomn, defaults to page->settings->meta description'
        )
    )

    fb_type = models.CharField(
        max_length=255,
        blank=True,
        default='website',
        verbose_name=_('Facebook Type'),
    )
    fb_title = models.CharField(
        max_length=255,
        blank=True,
        default='',
        verbose_name=_('Facebook title'),
    )
    fb_image = FilerImageField(
        null=True,
        blank=True,
        default=None,
        on_delete=models.SET_NULL,
        verbose_name=_('Facebook image'),
    )
    fb_description = models.TextField(
        max_length=355,
        blank=True,
        default='',
        verbose_name=_('Facebook description'),
    )
    fb_appid = models.CharField(
        max_length=255,
        blank=True,
        default='',
        verbose_name=_('Facebook app id'),
    )

    class Meta:
        verbose_name = _('Meta tags')
        verbose_name_plural = _('Meta tags')

    def __str__(self):
        return '{}'.format(self.get_meta_title())

    def get_meta_title(self):
        if self.meta_title:
            return '{}'.format(self.meta_title)
        if self.fb_title:
            return '{}'.format(self.fb_title)
        if self.placeholder.page:
            return '{}'.format(self.placeholder.page.get_page_title())
        return ''

    def get_meta_description(self):
        if self.meta_description:
            return '{}'.format(self.meta_description)
        if self.fb_description:
            return '{}'.format(self.fb_description)
        if self.placeholder.page:
            return '{}'.format(self.placeholder.page.get_meta_description())
        return ''

    def get_fb_type(self):
        return '{}'.format(self.fb_type or 'website')

    def get_fb_title(self):
        if self.fb_title:
            return '{}'.format(self.fb_title)
        return self.get_meta_title()

    def get_fb_description(self):
        if self.fb_description:
            return '{}'.format(self.fb_description)
        return self.get_meta_description()

    def get_fb_image(self):
        image = None
        if self.fb_image:
            image = self.fb_image
        if image:
            th = get_thumbnailer(image)
            return th.get_thumbnail(self.get_fb_image_options())
        return None

    def get_fb_image_options(self):
        return conf.FB_IMAGE_OPTIONS
