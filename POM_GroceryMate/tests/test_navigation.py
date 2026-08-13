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


def test_r07_pom_flow(logged_in_driver):
    """Verify the Page Object flow for creating a star-only review."""
    home_page = HomePage(logged_in_driver)
    store_page = home_page.go_to_shop()

    product_page = store_page.search_product("Loose Pears")

    assert product_page.get_title() == "Loose Pears"
    assert product_page.is_review_ui_displayed()

    initial_count = product_page.get_review_count()

    product_page.select_stars(3)
    product_page.send_review()

    final_count = product_page.wait_for_review_count_change(
        initial_count,
    )

    assert final_count == initial_count + 1
