# test_basic_parametrized.py
# Erstellt: 11.06.26 um 11:30
# Autor: natalya
# Projekt: Testautomatisierung


'''
### **Übung 1: Basis-Tests mit Parametrisierung**

Nutze Parametrisierung, um `count_word_matches` mit mehreren Eingabekombinationen aus
`text` und `target` sowie den erwarteten Ausgaben zu testen.

Schreibe einen parametrisierten Test, um die Funktion für einfache, gemischte und
einfache Randfallszenarien zu validieren.
'''

import pytest
from HW1_PyTest.word_counter import count_word_matches


@pytest.mark.parametrize(
        "text, target, expected", [
                ("The cat sat on the mat", "cat", 1),  # einfacher Fall
                ("Dog dog DOG dOg", "dog", 4),  # Groß-/Kleinschreibung ignoriert
                ("Hello world", "world", 1),  # einfaches Vorkommen
                ("hello hello HELLO", "hello", 3),  # mehrfaches Vorkommen, gemischt
                ("No matches here", "yes", 0),  # keine Übereinstimmung
                ("catcat cat catdog", "cat", 1),  # nur eigenständiges Wort zählt
                ("a a a", "a", 3),  # einzelnes Zeichen, mehrfach
                ]
        )
def test_count_word_matches_basic_cases(text, target, expected):
    assert count_word_matches(text, target) == expected
