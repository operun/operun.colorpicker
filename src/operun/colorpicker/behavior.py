# -*- coding: utf-8 -*-

from operun.colorpicker.widgets.widget import ColorPickerFieldWidget
from operun.colorpicker import _
from plone.autoform.interfaces import IFormFieldProvider
from plone.directives import form
from zope import schema
from zope.interface import alsoProvides


class IColorPickerBehavior(form.Schema):
    """
    A color picker field
    """

    color_picker = schema.TextLine(
        title=_(u"color_picker_title", default=u"Color Picker"),
        required=False,
        description=_(u"color_picker_description", default=u"Choose a color or enter a value."),  # noqa
    )

    form.widget(
        color_picker=ColorPickerFieldWidget,
    )

alsoProvides(IColorPickerBehavior, IFormFieldProvider)
