# base_page.py
# Erstellt: 22.07.26 um 14:00
# Autor: natalya
# Projekt: QA-Portfolio

import os
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from POM_GroceryMate.utils.constants import (
    URL_GROCERY_MATE,
    TIMEOUT_MEDIUM,
    SCREENSHOTS_DIR,
)


class BasePage:
    """Basisklasse für alle Page Objects"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, TIMEOUT_MEDIUM)

    def open(self):
        """Öffnet die Haupt-URL"""
        self.driver.get(URL_GROCERY_MATE)
        self.wait_for_page_load()
        return self

    def wait_for_page_load(self, timeout=TIMEOUT_MEDIUM):
        """Wartet bis die Seite geladen ist"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            return True
        except TimeoutException:
            self.take_screenshot("page_load_timeout")
            raise TimeoutException(
                f"Seite konnte nicht innerhalb von {timeout} Sekunden geladen werden"
            )

    def wait_for_element(self, locator, timeout=TIMEOUT_MEDIUM):
        """Wartet auf ein sichtbares Element"""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            self.take_screenshot(f"element_timeout")
            raise TimeoutException(
                f"Element {locator} nicht sichtbar innerhalb von {timeout} Sekunden"
            )

    def wait_for_elements(self, locator, timeout=TIMEOUT_MEDIUM):
        """Wartet auf alle sichtbaren Elemente"""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_all_elements_located(locator)
            )
        except TimeoutException:
            self.take_screenshot(f"elements_timeout")
            raise TimeoutException(
                f"Elemente {locator} nicht sichtbar innerhalb von {timeout} Sekunden"
            )

    def click_element(self, locator, timeout=TIMEOUT_MEDIUM):
        """Klickt auf ein Element"""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            element.click()
            return self
        except TimeoutException:
            self.take_screenshot(f"click_timeout")
            raise TimeoutException(
                f"Element {locator} nicht klickbar innerhalb von {timeout} Sekunden"
            )
        except Exception as e:
            self.take_screenshot(f"click_error")
            raise Exception(f"Fehler beim Klick auf {locator}: {str(e)}")

    def get_text(self, locator, timeout=TIMEOUT_MEDIUM):
        """Gibt den Text eines Elements zurück"""
        element = self.wait_for_element(locator, timeout)
        return element.text.strip()

    def enter_text(self, locator, text, timeout=TIMEOUT_MEDIUM):
        """Fügt Text in ein Eingabefeld ein"""
        try:
            element = self.wait_for_element(locator, timeout)
            element.clear()
            element.send_keys(text)
            return self
        except Exception as e:
            self.take_screenshot(f"input_error")
            raise Exception(f"Fehler beim Eingeben von Text in {locator}: {str(e)}")

    def is_element_present(self, locator, timeout=3):
        """Prüft ob ein Element vorhanden ist (kein Exception bei Fehler)"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def is_element_visible(self, locator, timeout=3):
        """Prüft ob ein Element sichtbar ist (kein Exception bei Fehler)"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def get_current_url(self):
        """Gibt die aktuelle URL zurück"""
        return self.driver.current_url

    def take_screenshot(self, name="screenshot"):
        """Macht einen Screenshot (stille Methode, kein Print)"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{SCREENSHOTS_DIR}{name}_{timestamp}.png"
        os.makedirs(SCREENSHOTS_DIR, exist_ok=True)
        self.driver.save_screenshot(filename)
        return filename

    def scroll_to_element(self, locator):
        """Scrollt zu einem Element"""
        try:
            element = self.wait_for_element(locator)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            return self
        except Exception as e:
            raise Exception(f"Fehler beim Scrollen zu {locator}: {str(e)}")
