# test_task2_login_users.py
# Erstellt: 12.07.26 um 15:06
# Autor: natalya
# Projekt: QA-Portfolio

"""
Login mit allen Benutzern
@pytest.fixture
@pytest.mark.parametrize
"""
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

SAUCEDEMO_PASSWORD = "secret_sauce"


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    # Webseite öffnen
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()


@pytest.mark.parametrize(
    "username, expected_result",
    [
        ("standard_user", True),
        ("locked_out_user", False),
        ("problem_user", True),
        ("performance_glitch_user", True),
        ("error_user", True),
        ("visual_user", True),
    ]
)


def test_basic_login(driver, username, expected_result):
    # Login-Elemente finden
    username_field = driver.find_element(By.ID, "user-name")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    # Login durchführen
    username_field.send_keys(username)
    password_field.send_keys(SAUCEDEMO_PASSWORD)
    login_button.click()

    # Verifikation
    if expected_result:
        backpack = driver.find_element(
            By.XPATH,
            '//div[@data-test="inventory-item-name" and text()="Sauce Labs Backpack"]'
        )
        assert backpack.is_displayed()

    else:
        error_message = driver.find_element(
            By.CSS_SELECTOR,
            '[data-test="error"]'
        )
        assert error_message.is_displayed()
        assert "locked out" in error_message.text
