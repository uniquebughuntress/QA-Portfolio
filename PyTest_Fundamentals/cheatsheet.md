# PyTest Cheatsheet

## Testfunktion

```python
def test_addition():
    assert 2 + 2 == 4
```

---

## Test ausführen

```bash
pytest
```

Ausführliche Ausgabe:

```bash
pytest -v
```

Bestimmte Datei:

```bash
pytest test_example.py
```

Bestimmter Test:

```bash
pytest test_example.py::test_addition
```

---

## Assertions

```python
assert result == expected
assert value is None
assert value is True
assert value is False
assert item in collection
assert item not in collection
assert isinstance(obj, int)
```

---

## Parametrisierung

```python
import pytest

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),
        (5, 5, 10),
        (0, 1, 1),
    ],
)
def test_add(a, b, expected):
    assert a + b == expected
```

---

## Fixtures

```python
import pytest

@pytest.fixture
def sample_list():
    return []
```

Verwendung:

```python
def test_append(sample_list):
    sample_list.append(1)
    assert sample_list == [1]
```

---

## Scope einer Fixture

```python
@pytest.fixture(scope="function")
```

Mögliche Scopes:

- `function`
- `class`
- `module`
- `package`
- `session`

---

## Exceptions testen

```python
import pytest

with pytest.raises(ValueError):
    int("abc")
```

---

## Test überspringen

```python
import pytest

@pytest.mark.skip
def test_example():
    ...
```

Bedingt überspringen:

```python
@pytest.mark.skipif(condition, reason="...")
```

---

## Erwarteter Fehler

```python
@pytest.mark.xfail(reason="Known bug")
```

---

## Häufig verwendete Optionen

```bash
pytest -v
pytest -s
pytest -k login
pytest -m smoke
pytest --maxfail=1
pytest --tb=short
```

---

## Best Practices

- Eine Aussage (`assert`) pro fachlichem Verhalten
- Aussagekräftige Testnamen verwenden
- Fixtures zur Wiederverwendung nutzen
- Parametrisierung statt doppeltem Code
- Tests unabhängig voneinander halten
- Keine festen Testdaten, wenn Variabilität erforderlich ist

---

## Reihenfolge beim Schreiben eines Tests

1. Arrange
2. Act
3. Assert
