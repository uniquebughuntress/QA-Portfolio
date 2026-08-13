# -*- coding: utf-8 -*-
# tests/test_navigation.py
# Erstellt: 12.08.26 um 20:45
# Autor: natalya

"""Navigation smoke tests."""

from POM_GroceryMate.pages import store_page
from POM_GroceryMate.pages.home_page import HomePage
from POM_GroceryMate.tests.conftest import logged_in_driver

# def test_search_and_open_nectarines(logged_in_driver):
#     """Open Nectarines through the store search."""
#     home_page = HomePage(logged_in_driver)
#     store_page = home_page.go_to_shop()
#
#     product_page = store_page.search_product("Nectarines")
#
#     assert product_page.get_title() == "Nectarines"


#
#
# def test_r07_pom_flow(logged_in_driver):
#     """Verify the Page Object flow for creating a star-only review."""
#     home_page = HomePage(logged_in_driver)
#     store_page = home_page.go_to_shop()
#
#     product_page = store_page.search_product("Loose Pears")
#
#     assert product_page.get_title() == "Loose Pears"
#     assert product_page.is_review_ui_displayed()
#
#     initial_count = product_page.get_review_count()
#
#     product_page.select_stars(3)
#     product_page.send_review()
#
#     final_count = product_page.wait_for_review_count_change(
#         initial_count,
#     )
#
#     assert final_count == initial_count + 1


# def test_add_oranges_to_cart(logged_in_driver):
#     """Verify that a product can be added from the store grid."""
#     home_page = HomePage(logged_in_driver)
#     store_page = home_page.go_to_shop()
#
#     store_page.add_product_to_cart(
#         "Oranges",
#         quantity=1,
#     )
#
#
# def test_select_fresh_vegetables(logged_in_driver):
#     """Verify that a product category can be selected."""
#     home_page = HomePage(logged_in_driver)
#     store_page = home_page.go_to_shop()
#
#     store_page.select_category("Fresh Vegetables")


# def test_add_oranges_from_fresh_vegetables(
#     logged_in_driver,
# ):
#     """Verify that a product can be added from a selected category."""
#     home_page = HomePage(logged_in_driver)
#     store_page = home_page.go_to_shop()
#
#     store_page.select_category("Fresh Vegetables")
#     store_page.add_product_to_cart(
#         "Oranges",
#         quantity=1,
#     )


# def test_add_prawns_from_frozen_foods(logged_in_driver):
#     """Verify that prawns can be added from the Frozen Foods category."""
#     home_page = HomePage(logged_in_driver)
#     store_page = home_page.go_to_shop()
#
#     store_page.select_category("Frozen Foods")
#     store_page.add_product_to_cart(
#         "Ocean Sea King Prawns",
#         quantity=2,
#     )


def test_open_checkout_from_cart(logged_in_driver):
    """Verify cart cleanup and checkout totals."""
    home_page = HomePage(logged_in_driver)

    # Open checkout and clean up existing basket data.
    checkout_page = home_page.go_to_checkout()

    while checkout_page.get_product_count() > 0:
        checkout_page.remove_first_product()

    assert checkout_page.get_product_count() == 0

    # Reopen checkout to verify that the basket is really empty.
    checkout_page = home_page.go_to_checkout()

    assert checkout_page.get_product_count() == 0

    # Add exactly one Orange.
    store_page = checkout_page.go_to_shop()

    store_page.add_product_to_cart(
        "Oranges",
        quantity=1,
    )

    # Open checkout again and verify the expected totals.
    checkout_page = home_page.go_to_checkout()

    assert checkout_page.get_product_count() == 1
    assert checkout_page.get_product_total() == "0.89€"
    assert checkout_page.get_shipping_cost() == 5.0
    assert checkout_page.get_total() == 5.89
