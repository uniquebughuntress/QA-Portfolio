# test_task3_user_registration.py
# Erstellt: 14.07.26 um 09:07
# Autor: natalya
# Projekt: QA-Portfolio


"""
Aufgabe 3: Registrierung eines neuen Benutzers.

Der Test führt den vollständigen Registrierungsprozess auf
https://automationexercise.com durch, überprüft den erfolgreichen
Login und löscht den neu angelegten Benutzer anschließend wieder.
"""

import uuid

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait


@pytest.fixture
def driver():
    """Stellt für jeden Test eine neue Firefox-Instanz bereit."""

    # Eigenes Firefox-Profil mit uBlock Origin verwenden.
    options = Options()

    options.profile = (
        "/Users/natalya/Library/Application Support/"
        "Firefox/Profiles/y9p26osy.selenium-profile"
    )

    driver = webdriver.Firefox(options=options)

    driver.maximize_window()
    driver.get("https://automationexercise.com/")

    yield driver

    driver.quit()


def test_register_new_user(driver):
    """Testet die vollständige Benutzerregistrierung."""
    wait = WebDriverWait(driver, 15)

    # Eindeutige E-Mail-Adresse für jeden Testlauf erzeugen.
    email = f"qa_{uuid.uuid4().hex[:10]}@example.com"
    # Startseite überprüfen.
    assert "Automation Exercise" in driver.title
    # Zur Registrierungsseite navigieren.
    driver.find_element(
        By.XPATH, '//a[@href="/login" and contains(.,"Signup / Login")]'
    ).click()
    wait.until(
        EC.visibility_of_element_located((By.XPATH, '//h2[text()="New User Signup!"]'))
    )
    # Neuen Benutzer anlegen.
    driver.find_element(By.CSS_SELECTOR, '[data-qa="signup-name"]').send_keys(
        "TestUser"
    )
    driver.find_element(By.CSS_SELECTOR, '[data-qa="signup-email"]').send_keys(email)
    driver.find_element(By.CSS_SELECTOR, '[data-qa="signup-button"]').click()

    wait.until(
        EC.visibility_of_element_located((By.XPATH, '//b[contains(.,"Enter Account")]'))
    )
    # Kontoinformationen ausfüllen.
    driver.find_element(By.ID, "id_gender1").click()
    driver.find_element(By.CSS_SELECTOR, '[data-qa="password"]').send_keys("Test123!")

    Select(driver.find_element(By.CSS_SELECTOR, '[data-qa="days"]')).select_by_value(
        "15"
    )
    Select(driver.find_element(By.CSS_SELECTOR, '[data-qa="months"]')).select_by_value(
        "6"
    )
    Select(driver.find_element(By.CSS_SELECTOR, '[data-qa="years"]')).select_by_value(
        "1990"
    )
    # Newsletter und Sonderangebote aktivieren.
    driver.find_element(By.ID, "newsletter").click()
    driver.find_element(By.ID, "optin").click()
    # Adressdaten ausfüllen
    driver.find_element(By.CSS_SELECTOR, '[data-qa="first_name"]').send_keys("Max")
    driver.find_element(By.CSS_SELECTOR, '[data-qa="last_name"]').send_keys(
        "Mustermann"
    )
    driver.find_element(By.CSS_SELECTOR, '[data-qa="company"]').send_keys(
        "QA Portfolio"
    )
    driver.find_element(By.CSS_SELECTOR, '[data-qa="address"]').send_keys(
        "Teststraße 123"
    )
    driver.find_element(By.CSS_SELECTOR, '[data-qa="address2"]').send_keys("Haus 5")
    Select(
        driver.find_element(By.CSS_SELECTOR, '[data-qa="country"]')
    ).select_by_visible_text("Canada")
    driver.find_element(By.CSS_SELECTOR, '[data-qa="state"]').send_keys("Ontario")
    driver.find_element(By.CSS_SELECTOR, '[data-qa="city"]').send_keys("Toronto")
    driver.find_element(By.CSS_SELECTOR, '[data-qa="zipcode"]').send_keys("M5A 1A1")
    driver.find_element(By.CSS_SELECTOR, '[data-qa="mobile_number"]').send_keys(
        "+49123456789"
    )
    # Benutzerkonto erstellen.
    driver.find_element(By.CSS_SELECTOR, '[data-qa="create-account"]').click()
    wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '[data-qa="account-created"]')
        )
    )
    # Erfolgreiche Kontoerstellung überprüfen.
    driver.find_element(By.CSS_SELECTOR, '[data-qa="continue-button"]').click()
    # Anmeldung des neuen Benutzers überprüfen.
    wait.until(
        EC.visibility_of_element_located((By.XPATH, '//a[contains(.,"Logged in as")]'))
    )
    # Benutzerkonto löschen.
    driver.find_element(By.XPATH, '//a[@href="/delete_account"]').click()
    wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '[data-qa="account-deleted"]')
        )
    )
    # Zur Startseite zurückkehren.
    driver.find_element(By.CSS_SELECTOR, '[data-qa="continue-button"]').click()
    assert "Automation Exercise" in driver.title
