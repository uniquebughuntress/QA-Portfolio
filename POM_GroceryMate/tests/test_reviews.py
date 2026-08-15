# -*- coding: utf-8 -*-
# tests/test_reviews.py
# Erstellt: 27.07.26 um 12:19
# Autor: natalya
# Projekt: QA-Portfolio
"""Review tests for GroceryMate."""

from POM_GroceryMate.pages import store_page
from POM_GroceryMate.pages.home_page import HomePage
from POM_GroceryMate.utils.constants import ProductPageLocators
import time


def test_create_star_only_review(logged_in_driver):
    """Verify that a user can submit a star-only review."""
    home_page = HomePage(logged_in_driver)
    store_page = home_page.go_to_shop()

    product_page = store_page.search_product("Cherries")

    assert product_page.get_title() == "Cherries"
    assert product_page.is_review_ui_displayed()

    initial_count = product_page.get_review_count()

    try:
        product_page.select_stars(3)
        product_page.send_review()

        final_count = product_page.wait_for_review_count_change(
            initial_count,
        )

        assert final_count == initial_count + 1
        assert product_page.get_first_author() == "Testina1"
        assert product_page.get_first_rating() == 3
        assert product_page.get_first_text() == ""

    finally:
        product_page.open_menu()
        product_page.click_delete()
        assert product_page.accept_alert()


def test_delete_own_review(logged_in_driver):
    """Verify that a user can delete their own review."""
    home_page = HomePage(logged_in_driver)
    store_page = home_page.go_to_shop()

    product_page = store_page.search_product("Loose Pears")

    initial_count = product_page.get_review_count()

    product_page.select_stars(3)
    product_page.send_review()

    created_count = product_page.wait_for_review_count_change(
        initial_count,
    )

    assert created_count == initial_count + 1
    assert product_page.get_first_author() == "Testina1"
    assert product_page.get_first_rating() == 3

    product_page.open_menu()
    product_page.click_delete()

    assert product_page.accept_alert()

    deleted_count = product_page.wait_for_review_count_change(
        created_count,
    )

    assert deleted_count == initial_count


def test_review_restriction_after_creation(logged_in_driver):
    """Verify that the review form is restricted after submitting a review."""
    home_page = HomePage(logged_in_driver)
    store_page = home_page.go_to_shop()

    product_page = store_page.search_product("Cherries")

    print("\n=== REVIEW RESTRICTION CHECK ===")
    print("Product:", product_page.get_title())
    print(
        "Review UI before:",
        product_page.is_review_ui_displayed(),
    )

    initial_count = product_page.get_review_count()
    print("Initial review count:", initial_count)

    product_page.select_stars(3)
    product_page.send_review()

    final_count = product_page.wait_for_review_count_change(
        initial_count,
    )

    assert final_count == initial_count + 1
    assert not product_page.is_review_ui_displayed()
    assert product_page.is_restriction_displayed()
    assert (
        product_page.get_restriction_text() == "You have already reviewed this product."
    )
