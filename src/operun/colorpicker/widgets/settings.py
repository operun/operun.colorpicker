# -*- coding: utf-8 -*-

from operun.colorpicker.misc import IColorpickerControlPanel
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.z3cform import layout


class ColorpickerPanelForm(RegistryEditForm):
    schema = IColorpickerControlPanel
    schema_prefix = 'colorpicker'
    label = u'Colorpicker Settings'


ColorpickerPanelView = layout.wrap_form(ColorpickerPanelForm, ControlPanelFormWrapper)
