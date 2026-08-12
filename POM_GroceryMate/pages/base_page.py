# -*- coding: utf-8 -*-
# pages/base_page.py
# Erstellt: 27.06.26 um 13:29
# Autor: natalya
# Projekt: QA-Portfolio

"""Base Page Object for the GroceryMate application."""

from selenium.common.exceptions import (
    NoAlertPresentException,
    TimeoutException,
)
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from POM_GroceryMate.utils.constants import (
    DEFAULT_TIMEOUT,
    SHORT_TIMEOUT,
    URL_GROCERY_MATE,
)


class BasePage:
    """Base class for all Page Objects."""

    def __init__(self, driver):
        """Initialize the Page Object."""
        self.driver = driver
        self.default_timeout = DEFAULT_TIMEOUT
        self.wait = WebDriverWait(
            self.driver,
            self.default_timeout,
        )

    def open(self, url: str = URL_GROCERY_MATE):
        """Open a URL and return this Page Object."""
        self.driver.get(url)
        return self

    def find_element(self, locator, timeout: int | None = None):
        """Return a present element."""
        timeout = self.default_timeout if timeout is None else timeout

        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def find_elements(self, locator, timeout: int | None = None):
        """Return all matching elements."""
        timeout = self.default_timeout if timeout is None else timeout

        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return self.driver.find_elements(*locator)
        except TimeoutException:
            return []

    def wait_for_element(self, locator, timeout: int | None = None):
        """Wait until an element is visible."""
        timeout = self.default_timeout if timeout is None else timeout

        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_clickable(self, locator, timeout: int | None = None):
        """Wait until an element is clickable."""
        timeout = self.default_timeout if timeout is None else timeout

        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def click(self, locator, timeout: int | None = None):
        """Click a clickable element."""
        element = self.wait_for_clickable(locator, timeout)
        element.click()

    def type_text(
        self,
        locator,
        text: str,
        clear_first: bool = True,
        timeout: int | None = None,
    ):
        """Enter text into a visible input."""
        element = self.wait_for_element(locator, timeout)

        if clear_first:
            element.clear()

        element.send_keys(text)

    def get_text(self, locator, timeout: int | None = None) -> str:
        """Return trimmed element text."""
        element = self.wait_for_element(locator, timeout)
        return element.text.strip()

    def is_element_visible(
        self,
        locator,
        timeout: int | None = None,
    ) -> bool:
        """Return whether an element is visible."""
        timeout = SHORT_TIMEOUT if timeout is None else timeout

        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def scroll_to_element(self, locator, timeout: int | None = None):
        """Scroll to an element."""
        element = self.wait_for_element(locator, timeout)

        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            element,
        )

    def refresh(self):
        """Refresh the current page."""
        self.driver.refresh()

    def get_current_url(self) -> str:
        """Return the current browser URL."""
        return self.driver.current_url

    def accept_alert(self, timeout: int | None = None) -> bool:
        """Accept a browser alert if one is present."""
        timeout = SHORT_TIMEOUT if timeout is None else timeout

        try:
            WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
            self.driver.switch_to.alert.accept()
            return True
        except (
            TimeoutException,
            NoAlertPresentException,
        ):
            return False
