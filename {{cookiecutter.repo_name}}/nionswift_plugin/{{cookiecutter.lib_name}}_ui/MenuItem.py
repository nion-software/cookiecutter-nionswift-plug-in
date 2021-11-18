import gettext
import logging
import typing

from {{cookiecutter.org_name}}.{{cookiecutter.lib_name}} import Processing

from nion.swift import Facade

_ = gettext.gettext


class MenuItemDelegate:
    def __init__(self, api: Facade.API_1) -> None:
        self.menu_id = "cookiecutter_menu"  # required, specify menu_id where this item will go
        self.menu_name = _("Cookiecutter")  # optional, specify default name if not a standard menu
        self.menu_before_id = "window_menu"  # optional, specify before menu_id if not a standard menu
        self.__menu_item_name = _("My Menu Item")  # menu item name
        self.__api = api

    def close(self) -> None:
        # close will be called if the extension is unloaded.
        pass

    @property
    def menu_item_name(self) -> str:
        return self.__menu_item_name

    def menu_item_execute(self, document_controller: Facade.DocumentWindow) -> None:
        self.__api.show(Processing.get_processing_data())
        logging.info("MenuItemDelegate menu_item_execute has been called.")


class MenuExampleExtension:
    # required for Swift to recognize this as an extension class.
    extension_id = "{{cookiecutter.org_name}}.{{cookiecutter.lib_name}}"

    def __init__(self, api_broker: typing.Any) -> None:
        # grab the api object.
        api = typing.cast(Facade.API_1, api_broker.get_api(version="~1.0"))
        # be sure to keep a reference or it will be closed immediately.
        self.__menu_item_ref = api.create_menu_item(MenuItemDelegate(api))

    def close(self) -> None:
        # close will be called when the extension is unloaded. in turn, close any references so they get closed. this
        # is not strictly necessary since the references will be deleted naturally when this object is deleted.
        self.__menu_item_ref.close()
        self.__menu_item_ref = typing.cast(typing.Any, None)
