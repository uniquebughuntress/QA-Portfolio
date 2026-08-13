# -*- coding: utf-8 -*-
# tests/test_reviews.py
# Erstellt: 27.07.26 um 12:19
# Autor: natalya
# Projekt: QA-Portfolio
"""Review tests for GroceryMate."""

from POM_GroceryMate.pages.home_page import HomePage


def test_create_star_only_review(logged_in_driver):
    """Verify that a user can submit a star-only review."""
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
    assert product_page.get_first_author() == "Testina1"
    assert product_page.get_first_rating() == 3
    assert product_page.get_first_text() == ""
