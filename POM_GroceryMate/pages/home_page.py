# -*- coding: utf-8 -*-
# pages/home_page.py
# Erstellt: 11.07.26 um 13:30
# Autor: natalya
# Projekt: QA-Portfolio

"""Page Object for the GroceryMate home page."""

from POM_GroceryMate.pages.base_page import BasePage
from POM_GroceryMate.utils.constants import (
    HomePageLocators,
    URL_GROCERY_MATE,
)


class HomePage(BasePage):
    """Page Object for the home page."""

    def open(self):
        """Open the home page."""
        super().open(URL_GROCERY_MATE)
        return self

    def go_to_shop(self):
        """Navigate to the store page."""
        self.click(HomePageLocators.NAV_SHOP)

        from POM_GroceryMate.pages.store_page import StorePage

        store_page = StorePage(self.driver)
        store_page.handle_age_verification()

        return store_page

    def go_to_favorites(self):
        """Navigate to the favorites page."""
        self.click(HomePageLocators.NAV_FAVORITES)

        from POM_GroceryMate.pages.store_page import StorePage

        return StorePage(self.driver)

    def is_logo_displayed(self) -> bool:
        """Return whether the logo is visible."""
        return self.is_element_visible(
            HomePageLocators.LOGO,
        )
