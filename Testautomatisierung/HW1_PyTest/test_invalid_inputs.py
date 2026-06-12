# test_invalid_inputs.py
# Erstellt: 11.06.26 um 11:31
# Autor: natalya
# Projekt: QA-Portfolio


'''
### Übung 3: Negativtests (Negative Testing)

Teste die Funktion auf ungültige Eingaben wie `None`, Ganzzahlen oder Listen,
um sicherzustellen, dass sie die entsprechenden Ausnahmen (Exceptions) auslöst.

Verwende ein Fixture, um Testfälle für ungültige Eingaben bereitzustellen.
'''

import pytest
from HW1_PyTest.word_counter import count_word_matches


@pytest.fixture
def invalid_inputs():
    """Liefert ungültige Eingaben als Liste von (text, target, expected_exception_or_value)."""
    return [
            (None, "word", None),  # text=None  → erwartet 0
            ("hello world", None, None),  # target=None → erwartet 0
            (123, "word", AttributeError),  # text als int
            ("hello world", 456, AttributeError),  # target als int
            (["hello", "world"], "world", AttributeError),  # text als Liste
            ("hello world", ["world"], AttributeError),  # target als Liste
            ]


@pytest.mark.parametrize("index", range(6))
def test_count_word_matches_invalid_inputs(invalid_inputs, index):
    text, target, expectation = invalid_inputs[index]
    
    if expectation is None:
        # None-Eingaben: Funktion soll 0 zurückgeben
        assert count_word_matches(text, target) == 0
    else:
        # Ungültige Typen: Funktion soll AttributeError auslösen
        with pytest.raises(expectation):
            count_word_matches(text, target)
