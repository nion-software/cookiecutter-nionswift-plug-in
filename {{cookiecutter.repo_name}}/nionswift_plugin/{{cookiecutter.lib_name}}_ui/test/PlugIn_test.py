import unittest

from {{cookiecutter.org_name}}.{{cookiecutter.lib_name}} import Processing
from nionswift_plugin.{{cookiecutter.lib_name}}_ui import MenuItem

from nion.swift import Facade


class TestLibrary(unittest.TestCase):

    def setUp(self) -> None:
        """Common code for all tests can go here."""
        pass

    def tearDown(self) -> None:
        """Common code for all tests can go here."""
        pass

    def test_menu_item_name(self) -> None:
        api = Facade.get_api("~1.0", "~1.0")
        self.assertEqual("cookiecutter_menu", MenuItem.MenuItemDelegate(api).menu_id)
