# PyTest – Interview Questions

## 1. Warum wird PyTest häufig gegenüber unittest bevorzugt?

### Musterantwort

PyTest bietet eine einfachere Syntax, leistungsfähige Assertions, Fixtures zur Wiederverwendung von Testdaten sowie eine integrierte Parametrisierung. Dadurch lassen sich Tests lesbarer und wartbarer schreiben als mit dem Standardmodul `unittest`.

---

## 2. Was ist eine Fixture?

### Musterantwort

Eine Fixture stellt Testdaten oder Testressourcen bereit und ermöglicht deren Wiederverwendung in mehreren Tests. Dadurch wird doppelter Code vermieden und Tests bleiben unabhängig voneinander.

---

## 3. Wann würdest du Parametrisierung verwenden?

### Musterantwort

Wenn dieselbe Testlogik mit verschiedenen Eingabewerten überprüft werden soll. Dadurch reduziert sich redundanter Code und neue Testfälle lassen sich einfach ergänzen.

---

## 4. Warum sind unabhängige Tests wichtig?

### Musterantwort

Jeder Test sollte isoliert ausführbar sein und nicht vom Ergebnis anderer Tests abhängen. Dadurch bleiben Testläufe reproduzierbar und Fehler lassen sich leichter analysieren.

---

## 5. Wofür wird `pytest.raises()` verwendet?

### Musterantwort

Mit `pytest.raises()` wird überprüft, ob eine bestimmte Exception ausgelöst wird. Dadurch können auch Fehlerfälle gezielt getestet werden.

---

## 6. Was ist der Unterschied zwischen `skip` und `xfail`?

### Musterantwort

- `skip` überspringt einen Test vollständig.
- `xfail` kennzeichnet einen bekannten Fehler, dessen Fehlschlagen aktuell erwartet wird.

---

## 7. Wann würdest du eine Fixture mit `session`-Scope verwenden?

### Musterantwort

Wenn eine Ressource nur einmal für den gesamten Testlauf erstellt werden soll, beispielsweise eine Datenbankverbindung oder ein WebDriver.

---

## 8. Welche Eigenschaften zeichnen einen guten automatisierten Test aus?

### Musterantwort

Ein guter Test ist:

- eindeutig
- unabhängig
- reproduzierbar
- schnell
- gut lesbar
- leicht wartbar

---

## 9. Warum sollte Testcode denselben Qualitätsansprüchen genügen wie Produktivcode?

### Musterantwort

Testcode wird langfristig gepflegt und weiterentwickelt. Sauber strukturierter Testcode reduziert Wartungsaufwand, verbessert die Lesbarkeit und erhöht die Zuverlässigkeit der Testautomatisierung.

---

## 10. Welche Rolle spielt PyTest in einer CI/CD-Pipeline?

### Musterantwort

PyTest kann automatisiert bei jedem Commit oder Pull Request ausgeführt werden. Dadurch werden Fehler früh erkannt und die Softwarequalität kontinuierlich überwacht.
