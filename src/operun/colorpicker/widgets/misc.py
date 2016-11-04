# -*- coding: utf-8 -*-

from zope import schema
from zope.interface import Interface


class IColorpickerControlPanel(Interface):

    loadbootstrap = schema.TextLine(
        title=u"Bootstrap CSS/JS", description=u"Include Bootstrap resources, uncheck if in use already.")
