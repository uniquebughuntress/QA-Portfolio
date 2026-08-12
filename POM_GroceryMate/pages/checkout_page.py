# -*- coding: utf-8 -*-
# pages/checkout_page.py
# Erstellt: 11.07.26 um 13:12
# Autor: natalya
# Projekt: QA-Portfolio

"""Page Object for the GroceryMate checkout page."""

from selenium.webdriver.common.by import By

from POM_GroceryMate.pages.base_page import BasePage


class CheckoutPage(BasePage):
    """Page Object representing the checkout page."""

    BASKET_ITEMS = (
        By.CSS_SELECTOR,
        ".checkout-card-item-container",
    )
    PRODUCT_REMOVE = (
        By.CSS_SELECTOR,
        "a.remove-icon",
    )
    PRODUCT_QUANTITY_MINUS = (
        By.CSS_SELECTOR,
        "button.minus",
    )
    SHIPMENT_COST = (
        By.CSS_SELECTOR,
        ".shipment-container h5:last-child",
    )
    PRODUCT_TOTAL = (
        By.CSS_SELECTOR,
        ".product-total-container h5:last-child",
    )
    TOTAL = (
        By.CSS_SELECTOR,
        ".total-container h5:last-child",
    )
    FREE_SHIPMENT_MSG = (
        By.CSS_SELECTOR,
        ".free-shipment-message",
    )

    def get_product_count(self) -> int:
        """Return the number of products in the basket."""
        return len(self.find_elements(self.BASKET_ITEMS))

    def get_shipment_cost(self) -> str:
        """Return the displayed shipping cost."""
        return self.get_text(self.SHIPMENT_COST)

    def get_shipping_cost(self) -> float:
        """Return the shipping cost as a float."""
        text = self.get_shipment_cost()
        text = text.replace("€", "").strip()

        return float(text) if text else 0.0

    def get_product_total(self) -> str:
        """Return the displayed product total."""
        return self.get_text(self.PRODUCT_TOTAL)

    def get_total(self) -> str:
        """Return the displayed order total."""
        return self.get_text(self.TOTAL)

    def remove_product(self):
        """Remove the first product from the basket."""
        self.click(self.PRODUCT_REMOVE)
        return self

    def remove_first_product(self):
        """Remove the first basket item."""
        items = self.find_elements(self.BASKET_ITEMS)

        if items:
            items[0].find_element(
                *self.PRODUCT_REMOVE,
            ).click()

        return self

    def decrease_quantity(self):
        """Decrease the quantity of the first product."""
        self.click(self.PRODUCT_QUANTITY_MINUS)
        return self

    def is_free_shipment_message_displayed(self) -> bool:
        """Return whether the free-shipping message is visible."""
        return self.is_element_visible(
            self.FREE_SHIPMENT_MSG,
            timeout=3,
        )
