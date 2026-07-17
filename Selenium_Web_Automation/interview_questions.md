# Selenium Web Automation – Interview Questions

## 1. Warum wird Selenium häufig für Web-Testautomatisierung verwendet?

### Musterantwort

Selenium unterstützt mehrere Browser, Programmiersprachen und Betriebssysteme. Es eignet sich besonders für End-to-End-Tests von Webanwendungen.

---

## 2. Was ist der Unterschied zwischen find_element() und find_elements()?

### Musterantwort

- `find_element()` liefert genau ein Element oder wirft eine Exception.
- `find_elements()` liefert eine Liste, die auch leer sein kann.

---

## 3. Wann würdest du CSS-Selektoren und wann XPath verwenden?

### Musterantwort

CSS-Selektoren bevorzuge ich für einfache, gut identifizierbare Elemente. XPath verwende ich bei komplexen DOM-Beziehungen oder wenn anhand von Text selektiert werden muss.

---

## 4. Warum sind Explicit Waits besser als time.sleep()?

### Musterantwort

Explicit Waits warten nur solange wie nötig und machen Tests stabiler und schneller. `time.sleep()` wartet immer die vollständige Zeit und kann Tests unnötig verlangsamen.

---

## 5. Was ist der Unterschied zwischen Implicit Wait und Explicit Wait?

### Musterantwort

Implicit Wait gilt global für alle Elementsuchen. Explicit Wait wird gezielt für eine bestimmte Bedingung eingesetzt und bietet deutlich mehr Kontrolle.

---

## 6. Welche Locator-Reihenfolge würdest du bevorzugen?

### Musterantwort

1. ID
2. data-test
3. Name
4. CSS Selector
5. XPath

Die Entscheidung richtet sich nach Stabilität und Wartbarkeit.

---

## 7. Was macht den Page Object Model (POM)-Ansatz aus?

### Musterantwort

POM trennt die Seitenlogik von den Testfällen. Dadurch werden Tests besser wartbar, wiederverwendbar und leichter erweiterbar.

---

## 8. Wie gehst du mit dynamischen Webseiten um?

### Musterantwort

Ich verwende geeignete Wait-Strategien, stabile Locatoren und vermeide feste Wartezeiten (`time.sleep()`), soweit möglich.

---

## 9. Wie würdest du einen instabilen Selenium-Test analysieren?

### Musterantwort

Ich prüfe zunächst Waits, Locatoren, dynamische Inhalte, Browser-Konsole und Reproduzierbarkeit. Anschließend analysiere ich Screenshots oder Logs, um die Ursache einzugrenzen.

---

## 10. Welche Eigenschaften sollte ein guter automatisierter UI-Test besitzen?

### Musterantwort

Ein guter UI-Test ist stabil, unabhängig, gut lesbar, wartbar und möglichst robust gegenüber kleinen Layoutänderungen.
