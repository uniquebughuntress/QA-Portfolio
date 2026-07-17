# test_task2_login_users.py
# Erstellt: 12.07.26 um 15:06
# Autor: natalya
# Projekt: QA-Portfolio

"""
Aufgabe 2: Login-Test für alle SauceDemo-Benutzer.

Verwendet:
- pytest.fixture zur Verwaltung des WebDrivers
- pytest.mark.parametrize zum Testen aller verfügbaren Benutzer
"""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

SAUCEDEMO_PASSWORD = "secret_sauce"


@pytest.fixture
def driver():
    """Stellt für jeden Test eine neue Firefox-Instanz bereit."""
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()


@pytest.mark.parametrize(
    "username, login_successful",
    [
        ("standard_user", True),
        ("locked_out_user", False),
        ("problem_user", True),
        ("performance_glitch_user", True),
        ("error_user", True),
        ("visual_user", True),
    ],
)
def test_basic_login(driver, username, login_successful):

    username_field = driver.find_element(By.ID, "user-name")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username_field.send_keys(username)
    password_field.send_keys(SAUCEDEMO_PASSWORD)
    login_button.click()

    # Je nach erwartetem Ergebnis unterschiedliche Verifikation durchführen.
    if login_successful:
        backpack = driver.find_element(
            By.XPATH,
            '//div[@data-test="inventory-item-name" and text()="Sauce Labs '
            'Backpack"]',
        )
        assert backpack.is_displayed()

    else:
        # Gesperrte Benutzer dürfen sich nicht anmelden.
        error_message = driver.find_element(By.CSS_SELECTOR, '[data-test="error"]')
        assert error_message.is_displayed()
        assert "locked out" in error_message.text
