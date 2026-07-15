# test_invalid_inputs.py
# Erstellt: 11.06.26 um 11:31
# Autor: natalya
# Projekt: QA-Portfolio


"""
Negativtests für die Funktion ``count_word_matches``.

Die Tests verwenden ein Fixture mit ungültigen Eingaben und überprüfen,
ob die Funktion entweder ``0`` zurückgibt oder die erwartete Exception
auslöst.
"""

import pytest
from HW1_PyTest.word_counter import count_word_matches


@pytest.fixture
def invalid_inputs():
    """Liefert ungültige Eingaben als Liste von Testfällen."""
    return [
        (None, "word", 0),
        ("hello world", None, 0),
        (123, "word", AttributeError),
        ("hello world", 456, AttributeError),
        (["hello", "world"], "world", AttributeError),
        ("hello world", ["world"], AttributeError),
    ]


def test_count_word_matches_invalid_inputs(invalid_inputs):
    """Testet das Verhalten bei ungültigen Eingaben."""

    for text, target, expectation in invalid_inputs:
        if expectation == 0:
            assert count_word_matches(text, target) == 0
        else:
            with pytest.raises(expectation):
                count_word_matches(text, target)
