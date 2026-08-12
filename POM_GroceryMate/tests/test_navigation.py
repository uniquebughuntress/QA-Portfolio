# -*- coding: utf-8 -*-
# tests/test_navigation.py
# Erstellt: 12.08.26 um 20:45
# Autor: natalya

"""Navigation smoke tests."""

from POM_GroceryMate.pages.home_page import HomePage


def test_search_and_open_nectarines(logged_in_driver):
    """Open Nectarines through the store search."""
    home_page = HomePage(logged_in_driver)
    store_page = home_page.go_to_shop()

    product_page = store_page.search_product("Nectarines")

    assert product_page.get_title() == "Nectarines"
