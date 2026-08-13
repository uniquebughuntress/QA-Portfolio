# -*- coding: utf-8 -*-
# tests/conftest.py
# Erstellt: 22.07.26 um 14:03
# Autor: natalya
# Projekt: QA-Portfolio

"""Shared pytest fixtures."""

import pytest
from selenium import webdriver

from POM_GroceryMate.pages.login_page import LoginPage
from POM_GroceryMate.pages.home_page import HomePage
from POM_GroceryMate.utils.constants import (
    TEST_USER_1_EMAIL,
    TEST_USER_1_PASSWORD,
    TEST_USER_2_EMAIL,
    TEST_USER_2_PASSWORD,
    URL_GROCERY_MATE,
)


@pytest.fixture
def driver():
    """Create and close a fresh Firefox browser per test."""
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(URL_GROCERY_MATE)

    yield driver

    driver.quit()


@pytest.fixture
def logged_in_driver(driver):
    """Return a browser logged in as Testina1."""
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login(
        TEST_USER_1_EMAIL,
        TEST_USER_1_PASSWORD,
    )

    return driver


@pytest.fixture
def logged_in_driver_test2(driver):
    """Return a browser logged in as Jenny Doe."""
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login(
        TEST_USER_2_EMAIL,
        TEST_USER_2_PASSWORD,
    )

    return driver


@pytest.fixture
def clean_cart(logged_in_driver):
    """Empty the shopping cart after the test."""
    yield logged_in_driver

    home_page = HomePage(logged_in_driver)
    checkout_page = home_page.go_to_checkout()

    while checkout_page.get_product_count() > 0:
        checkout_page.remove_first_product()
