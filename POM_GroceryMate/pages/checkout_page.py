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
    STREET_INPUT = (
        By.CSS_SELECTOR,
        "input[name='street']",
    )

    CITY_INPUT = (
        By.CSS_SELECTOR,
        "input[name='city']",
    )

    POSTAL_CODE_INPUT = (
        By.CSS_SELECTOR,
        "input[name='postalCode']",
    )

    CARD_NUMBER_INPUT = (
        By.CSS_SELECTOR,
        "input[name='cardNumber']",
    )

    NAME_ON_CARD_INPUT = (
        By.CSS_SELECTOR,
        "input[name='nameOnCard']",
    )

    EXPIRATION_INPUT = (
        By.CSS_SELECTOR,
        "input[name='expiration']",
    )

    CVV_INPUT = (
        By.CSS_SELECTOR,
        "input[name='cvv']",
    )

    BASKET_ITEMS = (
        By.CSS_SELECTOR,
        ".basket-items-container > .d-flex > .checkout-card-item-container",
    )

    SHOP_NAV = (
        By.XPATH,
        "//ul[@class='anim-nav']//a[@href='/store']",
    )

    PRODUCT_ITEM_BY_NAME = (
        By.XPATH,
        "//div[contains(@class, 'checkout-card-item-container')]"
        "[.//h5[contains(@class, 'checkout-product-title')"
        " and normalize-space()='{product_name}']]",
    )

    PRODUCT_QUANTITY_PLUS = (
        By.CSS_SELECTOR,
        "button.plus",
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

    def get_total(self) -> float:
        """Return the order total as a float."""
        text = self.get_text(self.TOTAL)
        text = text.replace("€", "").strip()

        return float(text) if text else 0.0

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

    def go_to_shop(self):
        """Navigate back to the shop."""
        self.click(self.SHOP_NAV)

        from POM_GroceryMate.pages.store_page import StorePage

        return StorePage(self.driver)

    def increase_quantity(
        self,
        product_name: str,
        times: int = 1,
    ):
        """Increase the quantity of a specific product."""
        if times < 1:
            raise ValueError("Times must be at least 1.")

        item_locator = (
            self.PRODUCT_ITEM_BY_NAME[0],
            self.PRODUCT_ITEM_BY_NAME[1].format(
                product_name=product_name,
            ),
        )

        item = self.find_element(item_locator)

        plus_button = item.find_element(
            *self.PRODUCT_QUANTITY_PLUS,
        )

        for _ in range(times):
            plus_button.click()

        return self
