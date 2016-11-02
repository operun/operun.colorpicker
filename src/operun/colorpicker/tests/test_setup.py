# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from operun.colorpicker.testing import OPERUN_COLORPICKER_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that operun.colorpicker is properly installed."""

    layer = OPERUN_COLORPICKER_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if operun.colorpicker is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'operun.colorpicker'))

    def test_browserlayer(self):
        """Test that IOperunColorpickerLayer is registered."""
        from operun.colorpicker.interfaces import (
            IOperunColorpickerLayer)
        from plone.browserlayer import utils
        self.assertIn(IOperunColorpickerLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = OPERUN_COLORPICKER_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['operun.colorpicker'])

    def test_product_uninstalled(self):
        """Test if operun.colorpicker is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'operun.colorpicker'))

    def test_browserlayer_removed(self):
        """Test that IOperunColorpickerLayer is removed."""
        from operun.colorpicker.interfaces import IOperunColorpickerLayer
        from plone.browserlayer import utils
        self.assertNotIn(IOperunColorpickerLayer, utils.registered_layers())
