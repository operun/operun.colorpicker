# -*- coding: utf-8 -*-

import zope.component
import zope.interface
import zope.schema.interfaces
from z3c.form import interfaces, widget
from z3c.form.browser import text


class IColorPickerWidget(interfaces.IWidget):
    """
    Color picker widget.
    """


class ColorPickerWidget(text.TextWidget):
    """
    Color picker widget.
    """
    zope.interface.implementsOnly(IColorPickerWidget)


def ColorPickerFieldWidget(field, request):
    """
    IFieldWidget factory for ColorPickerWidget.
    """
    return widget.FieldWidget(field, ColorPickerWidget(request))
