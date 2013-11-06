# -*- coding: utf-8 -*-

from zope import schema
from zope.interface import Interface
from allowed.domains import _


class IAllowedDomainsSettings(Interface):

    """ Allowed domains
    """

    allowed_domains = schema.List(value_type=schema.TextLine(),
                                  title=_(u'Allowed domains'),
                                  description=_(u'List of allowed domains when registering users. One domain per line.'),
                                  required=False)

