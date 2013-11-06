from plone.app.registry.browser import controlpanel
from allowed.domains.interfaces import IAllowedDomainsSettings
from allowed.domains import _


class AllowedDomainsSettingsEditForm(controlpanel.RegistryEditForm):

    schema = IAllowedDomainsSettings
    label = _(u"Allowed Domains Settings")
    description = _(u"""Settings for Allowed Domains""")

    def updateFields(self):
        super(AllowedDomainsSettingsEditForm, self).updateFields()

    def updateWidgets(self):
        super(AllowedDomainsSettingsEditForm, self).updateWidgets()


class AllowedDomainsSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    form = AllowedDomainsSettingsEditForm
