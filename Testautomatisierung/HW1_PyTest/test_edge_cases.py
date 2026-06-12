# test_edge_cases.py
# Erstellt: 11.06.26 um 11:30
# Autor: natalya
# Projekt: Testautomatisierung


'''
### Übung 2: Testen von Randfällen (Edge Case Testing)

Erstelle ein Fixture, das häufige Randfall-Eingaben bereitstellt, und teste die
Funktion mit parametrisierten Tests.

Fokussiere auf leere Eingaben, Leerzeichen und Interpunktion.
'''

import pytest
from HW1_PyTest.word_counter import count_word_matches


@pytest.fixture
def edge_case_inputs():
    """Liefert Randfall-Eingaben als Liste von (text, target, expected)."""
    return [
            ("", "word", 0),  # leerer Text
            ("hello world", "", 0),  # leeres Zielwort
            ("", "", 0),  # beides leer
            ("hello  world", "world", 1),  # mehrere Leerzeichen zwischen Wörtern
            (" cat ", "cat", 1),  # führende/nachgestellte Leerzeichen
            ("cat,dog cat", "cat", 1),  # Komma kein Trennzeichen → "cat,dog" ≠ "cat"
            ("x y z", "x", 1),  # einzelnes Zeichen
            ]


@pytest.mark.parametrize("index", range(7))
def test_count_word_matches_edge_cases(edge_case_inputs, index):
    text, target, expected = edge_case_inputs[index]
    assert count_word_matches(text, target) == expected
