# test_age_verification.py
# Erstellt: 27.07.26 um 12:21
# Autor: natalya
# Projekt: QA-Portfolio

import pytest

from POM_GroceryMate.pages.store_page import StorePage
from POM_GroceryMate.utils.constants import URL_SHOP
from POM_GroceryMate.utils.test_data import (
    get_age_verification_dates,
)


@pytest.mark.alcohol
def test_a01_age_verification_exactly_18(driver):
    """Verify that exactly 18 years grants access to alcohol products."""
    eighteenth_birthday, _ = get_age_verification_dates()

    driver.get(URL_SHOP)
    store_page = StorePage(driver)

    assert store_page.is_age_verification_displayed()

    store_page.verify_age(eighteenth_birthday)

    assert store_page.is_success_toast_displayed()
    assert (
        store_page.get_toast_message()
        == "You are of age. You can now view all products, "
        "even alcohol products."
    )


@pytest.mark.alcohol
def test_a02_age_verification_under_18(driver):
    """Verify that 17 years and 364 days is treated as underage."""
    _, underage_boundary = get_age_verification_dates()

    driver.get(URL_SHOP)
    store_page = StorePage(driver)

    assert store_page.is_age_verification_displayed()

    store_page.verify_age(underage_boundary)

    assert store_page.is_error_toast_displayed()
    assert (
        store_page.get_toast_message()
        == "You are underage. You can still browse the site, "
        "but you will not be able to view alcohol products."
    )
