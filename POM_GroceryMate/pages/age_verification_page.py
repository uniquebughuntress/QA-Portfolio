# -*- coding: utf-8 -*-
# pages/age_verification_page.py
# Erstellt: 11.07.26 um 13:31
# Autor: natalya
# Projekt: QA-Portfolio

"""Page Object for the age verification modal."""

from selenium.webdriver.common.by import By

from POM_GroceryMate.pages.base_page import BasePage


class AgeVerificationPage(BasePage):
    """Page Object for the age verification modal."""

    MODAL_OVERLAY = (
        By.CSS_SELECTOR,
        "div.modal-overlay",
    )
    MODAL_INPUT = (
        By.CSS_SELECTOR,
        ".modal-content input[type='text']",
    )
    MODAL_CONFIRM_BTN = (
        By.XPATH,
        "//div[@class='modal-content']//button[text()='Confirm']",
    )
    MODAL_TEXT = (
        By.CSS_SELECTOR,
        ".modal-content p",
    )

    def is_displayed(self) -> bool:
        """Return whether the age verification modal is visible."""
        return self.is_element_visible(self.MODAL_OVERLAY)

    def enter_birth_date(self, birth_date: str):
        """Enter a birth date into the modal."""
        self.type_text(self.MODAL_INPUT, birth_date)
        return self

    def confirm(self):
        """Confirm the entered birth date."""
        self.click(self.MODAL_CONFIRM_BTN)
        return self

    def get_message(self) -> str:
        """Return the modal message."""
        return self.get_text(self.MODAL_TEXT)
