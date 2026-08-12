# -*- coding: utf-8 -*-
# pages/login_page.py
# Erstellt: 11.07.26 um 15:06
# Autor: natalya
# Projekt: QA-Portfolio

"""Page Object for the GroceryMate login page."""

from POM_GroceryMate.pages.base_page import BasePage
from POM_GroceryMate.utils.constants import (
    LoginPageLocators,
    URL_LOGIN,
)


class LoginPage(BasePage):
    """Page Object representing the login page."""

    def open(self, url: str = URL_LOGIN):
        """Open the login page."""
        return super().open(url)

    def login(self, email: str, password: str):
        """Log in and return the Home Page."""
        self.type_text(
            LoginPageLocators.EMAIL_INPUT,
            email,
        )
        self.type_text(
            LoginPageLocators.PASSWORD_INPUT,
            password,
        )
        self.click(LoginPageLocators.SUBMIT_BTN)

        from POM_GroceryMate.pages.home_page import HomePage

        return HomePage(self.driver)

    def get_error_message(self) -> str:
        """Return the login error message."""
        if self.is_element_visible(
            LoginPageLocators.LOGIN_ERROR,
        ):
            return self.get_text(
                LoginPageLocators.LOGIN_ERROR,
            )

        return ""
