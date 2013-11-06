from Products.CMFCore.utils import getToolByName
from Products.PluggableAuthService.interfaces.authservice \
    import IPluggableAuthService
from Acquisition import aq_base, aq_chain
from zope.component import getUtility

import logging
logger = logging.getLogger(__name__)


def isMemberIdAllowed(self, id):
    if len(id) < 1 or id == 'Anonymous User':
        return 0
    if not self._ALLOWED_MEMBER_ID_PATTERN.match(id):
        return 0

    pas = getToolByName(self, 'acl_users')
    if IPluggableAuthService.providedBy(pas):
        results = pas.searchPrincipals(id=id, exact_match=True)
        if results:
            return 0
        else:
            for parent in aq_chain(self):
                if hasattr(aq_base(parent), "acl_users"):
                    parent = parent.acl_users
                    if IPluggableAuthService.providedBy(parent):
                        if parent.searchPrincipals(id=id,
                                                   exact_match=True):
                            return 0
        # When email addresses are used as logins, we need to check
        # if there are any users with the requested login.
        props = getToolByName(self, 'portal_properties').site_properties
        if props.use_email_as_login:
            results = pas.searchUsers(name=id, exact_match=True)
            if results:
                # return 0
                # *********************
                # Check if domain is ok
                # *********************
                from allowed.domains.interfaces import IAllowedDomainsSettings
                from plone.registry.interfaces import IRegistry
                registry = getUtility(IRegistry)
                settings = registry.forInterface(IAllowedDomainsSettings)
                # Assume validation has ensured there is a @ in the id
                if id.split('@')[1] in settings.allowed_domains:
                    return 0
                # *********************

    else:
        membership = getToolByName(self, 'portal_membership')
        if membership.getMemberById(id) is not None:
            return 0
        groups = getToolByName(self, 'portal_groups')
        if groups.getGroupById(id) is not None:
            return 0

    return 1
