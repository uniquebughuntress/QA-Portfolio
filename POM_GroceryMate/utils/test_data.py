# -*- coding: utf-8 -*-
# utils/test_data.py
# Erstellt: 26.07.26 um 16:53
# Autor: natalya
# Projekt: QA-Portfolio

"""Reusable test-data generators."""

from datetime import date, timedelta
import uuid

from faker import Faker

fake = Faker()


def generate_test_user() -> dict:
    """Generate a unique test user."""
    unique_id = uuid.uuid4().hex[:8]

    return {
        "name": f"QA_Test_{unique_id}",
        "email": f"qa_{unique_id}@example.com",
        "password": f"Test123!{unique_id[:4]}",
    }


def generate_review_text(length: int = 100) -> str:
    """Generate review text with the requested length."""
    if length <= 0:
        return ""

    base_text = (
        "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, "
        "sed diam nonumy eirmod tempor invidunt ut labore et dolore "
        "magna aliquyam erat, sed diam voluptua. "
    )

    while len(base_text) < length:
        base_text += base_text

    return base_text[:length]


def generate_birth_date(days_offset: int = 0) -> str:
    """
    Generate a birth date relative to the 18th birthday.

    Args:
        days_offset: Offset from the 18th birthday.
            0 = exactly 18 years old.
            1 = 17 years + 364 days.
            -1 = 18 years + 1 day.

    Returns:
        Birth date in DD-MM-YYYY format.
    """
    today = date.today()
    eighteenth_birthday = today.replace(year=today.year - 18)

    birth_date = eighteenth_birthday - timedelta(days=days_offset)

    return birth_date.strftime("%d-%m-%Y")


from datetime import date, timedelta


def get_age_verification_dates() -> tuple[str, str]:
    """Return dates for exactly 18 and 17 years + 364 days."""
    today = date.today()

    eighteenth_birthday = today.replace(
        year=today.year - 18,
    )

    underage_boundary = eighteenth_birthday + timedelta(days=1)

    return (
        eighteenth_birthday.strftime("%d-%m-%Y"),
        underage_boundary.strftime("%d-%m-%Y"),
    )
