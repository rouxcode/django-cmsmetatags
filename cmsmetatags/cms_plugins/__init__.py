from __future__ import unicode_literals

from cms.plugin_pool import plugin_pool

from .cms_metatags import CMSMetaTagsPlugin


plugin_pool.register_plugin(CMSMetaTagsPlugin)
