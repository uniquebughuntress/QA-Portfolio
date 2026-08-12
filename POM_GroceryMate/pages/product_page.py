# -*- coding: utf-8 -*-
# pages/product_page.py
# Erstellt: 22.07.26 um 14:06
# Autor: natalya
# Projekt: QA-Portfolio

"""Page Object for the GroceryMate product detail page."""

from selenium.webdriver.common.by import By

from POM_GroceryMate.pages.base_page import BasePage
from POM_GroceryMate.utils.constants import (
    DEFAULT_TIMEOUT,
    ProductPageLocators,
)


class ProductPage(BasePage):
    """Page Object for a product detail page."""

    def open_product(self, url: str):
        """Open a product URL."""
        self.driver.get(url)
        return self

    def get_title(self) -> str:
        """Return the product title."""
        try:
            return self.get_text(
                ProductPageLocators.PRODUCT_TITLE,
            )
        except Exception:
            return ""

    def add_to_cart(self):
        """Add the current product to the cart."""
        self.click(ProductPageLocators.ADD_TO_CART_BTN)
        return self

    # ==================== REVIEW UI ====================

    def is_review_ui_displayed(self) -> bool:
        """Return whether the review form is visible."""
        return self.is_element_visible(
            ProductPageLocators.REVIEW_TEXTAREA,
            timeout=3,
        )

    def is_restriction_displayed(self) -> bool:
        """Return whether the review restriction is visible."""
        return self.is_element_visible(
            ProductPageLocators.REVIEW_RESTRICTION,
            timeout=3,
        )

    def get_restriction_text(self) -> str:
        """Return the review restriction text."""
        try:
            return self.get_text(
                ProductPageLocators.REVIEW_RESTRICTION_TEXT,
            )
        except Exception:
            return ""

    def select_stars(self, count: int):
        """Select the requested number of review stars."""
        stars = self.find_elements(
            ProductPageLocators.REVIEW_STARS,
            timeout=DEFAULT_TIMEOUT,
        )

        for star in stars[:count]:
            star.click()

        return self

    def enter_review_text(self, text: str):
        """Enter review text."""
        self.type_text(
            ProductPageLocators.REVIEW_TEXTAREA,
            text,
        )
        return self

    def send_review(self):
        """Submit the review."""
        self.click(
            ProductPageLocators.REVIEW_SEND_BTN,
        )
        return self

    def submit_review(
        self,
        stars: int,
        text: str = "",
    ):
        """Submit a review with stars and optional text."""
        self.select_stars(stars)

        if text:
            self.enter_review_text(text)

        self.send_review()

        return self

    # ==================== COMMENT DATA ====================

    def get_first_author(self) -> str:
        """Return the author of the first comment."""
        try:
            return self.get_text(
                ProductPageLocators.FIRST_COMMENT_HEADER,
            )
        except Exception:
            return ""

    def get_first_text(self) -> str:
        """Return the text of the first comment."""
        try:
            return self.get_text(
                ProductPageLocators.FIRST_COMMENT_TEXT,
            )
        except Exception:
            return ""

    def get_first_rating(self) -> int:
        """Return the rating of the first comment."""
        stars = self.find_elements(
            ProductPageLocators.FIRST_COMMENT_RATING_STARS,
        )

        return sum(
            1
            for star in stars
            if (
                "full" in star.get_attribute("class")
                or "partial" in star.get_attribute("class")
            )
        )

    # ==================== REVIEW MENU ====================

    def open_menu(self):
        """Open the menu of the first comment."""
        self.scroll_to_element(
            ProductPageLocators.FIRST_COMMENT,
        )
        self.click(
            ProductPageLocators.FIRST_COMMENT_MENU_ICON,
        )
        return self

    def click_delete(self):
        """Click Delete in the comment menu."""
        self.click(
            ProductPageLocators.DROPDOWN_DELETE_BTN,
        )
        return self

    def delete_review(self):
        """Delete the first review and confirm the browser alert."""
        self.open_menu()
        self.click_delete()

        if not self.accept_alert():
            raise RuntimeError("Delete confirmation alert was not displayed.")

        return self
