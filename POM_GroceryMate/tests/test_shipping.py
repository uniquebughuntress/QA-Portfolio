# tests/test_shipping.py
# Erstellt: 27.07.26 um 12:22
# Autor: natalya
# Projekt: QA-Portfolio
from POM_GroceryMate.pages.home_page import HomePage


def test_shipping_v01(logged_in_driver):
    """Verify free shipping for an order total of exactly 20.00€."""
    home_page = HomePage(logged_in_driver)
    store_page = home_page.go_to_shop()

    store_page.select_category("Fresh Vegetables")
    store_page.add_product_to_cart("Oranges")

    store_page.select_category("Frozen Foods")
    store_page.add_product_to_cart(
        "Freshona Fruit Smoothie Mixes Assorted",
    )
    store_page.add_product_to_cart(
        "Ocean Sea King Prawns",
    )
    store_page.add_product_to_cart(
        "Trattoria Alfredo Margherita Pizza 3 Pack",
    )
    store_page.add_product_to_cart(
        "Double Ice Cream Caramel Sticks",
    )

    checkout_page = home_page.go_to_checkout()

    checkout_page.increase_quantity(
        "Ocean Sea King Prawns",
    )

    assert checkout_page.get_product_total() == "20.00€"
    assert checkout_page.get_shipping_cost() == 0.0
    assert checkout_page.get_total() == 20.0
