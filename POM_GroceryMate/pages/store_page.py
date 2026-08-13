# -*- coding: utf-8 -*-
# pages/store_page.py
# Erstellt: 12.07.26 um 14:14
# Autor: natalya
# Projekt: QA-Portfolio

"""Page Object for the GroceryMate store page."""

from selenium.webdriver.support import expected_conditions as EC

from POM_GroceryMate.pages.base_page import BasePage
from POM_GroceryMate.pages.product_page import ProductPage
from POM_GroceryMate.utils.constants import (
    StorePageLocators,
    URL_SHOP,
)
from POM_GroceryMate.utils.test_data import generate_birth_date
from selenium.webdriver.common.keys import Keys


class StorePage(BasePage):
    """Page Object for the GroceryMate store."""

    def open(self, url: str = URL_SHOP):
        """Open the store and handle age verification."""
        super().open(url)
        self.handle_age_verification()
        return self

    def handle_age_verification(self):
        """
        Handle the age verification modal when it is displayed.

        A valid age is used as a technical prerequisite for
        shopping-related tests.
        """
        if not self.is_element_visible(
            StorePageLocators.MODAL_OVERLAY,
        ):
            return self

        birth_date = generate_birth_date(0)

        self.type_text(
            StorePageLocators.MODAL_INPUT,
            birth_date,
        )
        self.click(
            StorePageLocators.MODAL_CONFIRM_BTN,
        )

        self.wait.until(
            EC.invisibility_of_element_located(
                StorePageLocators.MODAL_OVERLAY,
            )
        )

        return self

    def search_product(self, product_name: str):
        """Search for and open a product from the search suggestions."""
        self.type_text(
            StorePageLocators.SEARCH_INPUT,
            product_name,
        )

        suggestion_locator = (
            StorePageLocators.SEARCH_SUGGESTION_BY_NAME[0],
            StorePageLocators.SEARCH_SUGGESTION_BY_NAME[1].format(
                product_name=product_name,
            ),
        )

        self.click(suggestion_locator)

        return ProductPage(self.driver)

    def click_product_by_name(self, product_name: str):
        """Open a product through the store search."""
        return self.search_product(product_name)

    # def add_product_to_cart(
    #     self,
    #     product_name: str,
    #     quantity: int = 1,
    # ):
    #     """Add a product from the current grid to the cart."""
    #     if quantity < 1:
    #         raise ValueError("Quantity must be at least 1.")
    #
    #     card_locator = (
    #         StorePageLocators.PRODUCT_CARD_BY_NAME[0],
    #         StorePageLocators.PRODUCT_CARD_BY_NAME[1].format(
    #             product_name=product_name,
    #         ),
    #     )
    #
    #     card = self.find_element(card_locator)
    #
    #     quantity_input = card.find_element(
    #         *StorePageLocators.PRODUCT_QUANTITY,
    #     )
    #
    #     quantity_input.clear()
    #     quantity_input.send_keys(str(quantity))
    #     quantity_input.send_keys(Keys.TAB)
    #
    #     add_to_cart_button = card.find_element(
    #         *StorePageLocators.PRODUCT_ADD_TO_CART,
    #     )
    #
    #     add_to_cart_button.click()
    #
    #     return self

    def select_category(self, category_name: str):
        """Select a product category."""
        category_locator = (
            StorePageLocators.CATEGORY_BY_NAME[0],
            StorePageLocators.CATEGORY_BY_NAME[1].format(
                category_name=category_name,
            ),
        )

        self.click(category_locator)

        return self

    def add_product_to_cart(
        self,
        product_name: str,
    ):
        """Add one unit of a product from the current grid to the cart."""
        card_locator = (
            StorePageLocators.PRODUCT_CARD_BY_NAME[0],
            StorePageLocators.PRODUCT_CARD_BY_NAME[1].format(
                product_name=product_name,
            ),
        )

        card = self.find_element(card_locator)

        add_to_cart_button = card.find_element(
            *StorePageLocators.PRODUCT_ADD_TO_CART,
        )

        add_to_cart_button.click()

        return self
