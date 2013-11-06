Introduction
============

Sample of how to disable user registration for users from other domains than specified.

Content
=======

Nothing fancy:
 - Control panel view with list of allowed domains
 - Monkey patch for `Product.CMFPlone.RegistrationTool.RegistrationTool.isMemberIdAllowed` where the domain is checked against list of allowed domains
